# 🏨 Real-Time Hotel Booking Dashboard + 💬 RAG Chatbot

This project is an interactive **Streamlit dashboard** that simulates **real-time hotel bookings**, predicts booking cancellations, and includes a **RAG-based AI chatbot** trained on your own PDF documents (like Python, ML, SQL references). It blends **data simulation**, **ML inference**, and **AI retrieval-augmented generation** into a single web app.

---

## 🚀 Project Overview

### 🏨 Hotel Simulation Dashboard
- Simulates hotel bookings in real time.
- Displays:
  - Booking history
  - Cancellation predictions
  - Visualization of trends

### 💬 Chatbot Assistant (RAG-Based)
- Uses your **own PDF documentation** as context.
- Users can ask questions (e.g., “How does SQL JOIN work?”).
- Retrieves relevant text chunks using vector similarity (FAISS).
- Generates answers using a lightweight LLM (`distilgpt2`).

---

✨ Features
🔄 Auto Simulation toggle (choose speed)

📈 Live Visualization of cancellation trends

➕ Manual booking simulation

💬 RAG Chatbot using your PDF knowledge base


🧩 Additional Information Options:
📊 Project Use Cases / Benefits
What kind of real-world problems this dashboard solves?

Who might use it? (e.g., hotel managers, students, data analysts)

Why is combining simulation + prediction + RAG useful?

🔍 How Predictions Work (Optional ML Model Explanation)
Right now, predictions are random (placeholder).

You could easily plug in a trained ML model (joblib) to:

Predict cancellations

Predict total spend

Predict repeat guests


## 🧰 Tools and Technologies

| Component               | Tool / Library                    |
|------------------------|-----------------------------------|
| UI & Web App           | `Streamlit`                       |
| Embeddings             | `sentence-transformers`           |
| Vector Store           | `FAISS`                           |
| PDF Parsing            | `PyMuPDF` (`fitz`)                |
| Lightweight LLM        | `distilgpt2` via HuggingFace      |
| Dashboard Visuals      | `Streamlit DataFrame`, `bar_chart`|

---
