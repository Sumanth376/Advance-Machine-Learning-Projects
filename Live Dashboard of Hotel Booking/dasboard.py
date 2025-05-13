import streamlit as st
import pandas as pd
import random
from datetime import datetime
import os
import time
import fitz  # PyMuPDF
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

# ----------------- Load Models -----------------
@st.cache_resource
def load_models():
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    llm = pipeline("text-generation", model="distilgpt2", max_new_tokens=150)
    return embedder, llm

embedder, llm = load_models()

# ----------------- Load PDFs and Create FAISS Index -----------------
@st.cache_resource
def load_docs_and_index():
    pdf_dir = "docs"
    texts = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            with fitz.open(os.path.join(pdf_dir, filename)) as pdf:
                for page in pdf:
                    texts.append(page.get_text())

    chunks = []
    for text in texts:
        for i in range(0, len(text), 500):
            chunks.append(text[i:i+500])

    vectors = embedder.encode(chunks)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))

    return chunks, index

chunks, vector_index = load_docs_and_index()

# ----------------- Chatbot Function -----------------
def ask_chatbot(query):
    query_vec = embedder.encode([query])
    D, I = vector_index.search(query_vec, k=3)
    context = "\n".join([chunks[i] for i in I[0]])
    prompt = f"Answer the question based on the context:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    result = llm(prompt)[0]['generated_text']
    return result.split("Answer:")[-1].strip()

# ----------------- Booking Simulation Logic -----------------
hotels = ['The Grand Inn', 'Ocean View Resort', 'City Center Hotel', 'Mountain Lodge']
room_types = ['Standard', 'Deluxe', 'Suite']
channels = ['Website', 'App', 'Phone']
payment_methods = ['Credit Card', 'PayPal', 'UPI', 'Net Banking']
countries = ['India', 'USA', 'UK', 'Germany', 'Australia', 'Canada']

if 'bookings' not in st.session_state:
    st.session_state.bookings = pd.DataFrame()
if 'auto_simulate' not in st.session_state:
    st.session_state.auto_simulate = False
if 'last_sim_time' not in st.session_state:
    st.session_state.last_sim_time = time.time()

def predict_cancellation(booking):
    # Placeholder prediction logic: customize with your model later
    return random.choices([0, 1], weights=[0.8, 0.2])[0]

def generate_booking():
    price = round(random.uniform(50, 500), 2)
    nights = random.randint(1, 7)
    booking = {
        'booking_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hotel': random.choice(hotels),
        'room_type': random.choice(room_types),
        'price_per_night': price,
        'nights': nights,
        'total_price': round(price * nights, 2),
        'guests': random.randint(1, 4),
        'channel': random.choice(channels),
        'customer_age': random.randint(18, 70),
        'payment_method': random.choice(payment_methods),
        'country': random.choice(countries),
        'is_repeat_guest': random.choice([True, False]),
    }
    booking['Predicted_Cancellation'] = predict_cancellation(booking)
    return booking

# ----------------- Sidebar -----------------
st.sidebar.title("⚙️ Controls")
selected_hotel = st.sidebar.selectbox("Filter by Hotel", ["All"] + hotels)

if st.sidebar.button("➕ Manual Booking"):
    new_booking = generate_booking()
    st.session_state.bookings = pd.concat([
        st.session_state.bookings,
        pd.DataFrame([new_booking])
    ], ignore_index=True)
    st.sidebar.success("Booking added!")

# Real-time simulation controls
st.sidebar.markdown("---")
st.sidebar.subheader("📡 Real-Time Simulation")
simulate = st.sidebar.toggle("Auto Simulate", value=st.session_state.auto_simulate)
speed = st.sidebar.slider("Simulation speed (seconds)", 1, 10, 3)

st.session_state.auto_simulate = simulate

# Chat Assistant
with st.sidebar.expander("💬 Ask the Docs"):
    user_query = st.text_input("Your question:")
    if user_query:
        with st.spinner("Thinking..."):
            reply = ask_chatbot(user_query)
            st.success(reply)

# ----------------- Main Page -----------------
st.title("🏨 Real-Time Hotel Booking Dashboard + 💬 PDF Chatbot")

# Auto simulation logic
now = time.time()
if st.session_state.auto_simulate and now - st.session_state.last_sim_time > speed:
    booking = generate_booking()
    st.session_state.bookings = pd.concat([
        st.session_state.bookings,
        pd.DataFrame([booking])
    ], ignore_index=True)
    st.session_state.last_sim_time = now
    st.experimental_rerun()

# Filtered data
filtered_data = st.session_state.bookings
if selected_hotel != "All":
    filtered_data = filtered_data[filtered_data['hotel'] == selected_hotel]

if not filtered_data.empty:
    st.subheader("📋 Recent Bookings")
    st.dataframe(filtered_data.tail(10), use_container_width=True)

    st.subheader("📊 Cancellation Rate by Hotel")
    chart_data = filtered_data.groupby("hotel")["Predicted_Cancellation"].mean().reset_index()
    st.bar_chart(chart_data.set_index("hotel"))
else:
    st.info("No bookings yet. Use the sidebar to simulate one or enable Auto Simulate.")
