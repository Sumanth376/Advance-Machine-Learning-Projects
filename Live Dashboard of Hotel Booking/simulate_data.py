import pandas as pd
import random
from datetime import datetime, timedelta

# Simulation configuration
num_records = 10000

# Sample data
hotels = ['The Grand Inn', 'Ocean View Resort', 'City Center Hotel', 'Mountain Lodge']
room_types = ['Standard', 'Deluxe', 'Suite']
channels = ['Website', 'App', 'Phone']
statuses = ['Confirmed', 'Cancelled', 'Pending']
payment_methods = ['Credit Card', 'PayPal', 'UPI', 'Net Banking']
countries = ['India', 'USA', 'UK', 'Germany', 'Australia', 'Canada']

bookings = []

for _ in range(num_records):
    booking_time = datetime.now() - timedelta(days=random.randint(0, 365))
    price = round(random.uniform(50, 500), 2)
    nights = random.randint(1, 7)

    booking = {
        'booking_time': booking_time.strftime("%Y-%m-%d %H:%M:%S"),
        'hotel': random.choice(hotels),
        'room_type': random.choice(room_types),
        'price_per_night': price,
        'nights': nights,
        'total_price': round(price * nights, 2),
        'guests': random.randint(1, 4),
        'channel': random.choice(channels),
        'status': random.choices(statuses, weights=[0.7, 0.2, 0.1])[0],
        'customer_age': random.randint(18, 70),
        'payment_method': random.choice(payment_methods),
        'country': random.choice(countries),
        'is_repeat_guest': random.choice([True, False])
    }

    bookings.append(booking)

# Create DataFrame
df = pd.DataFrame(bookings)
df.to_csv('hotel_bookings.csv', index=False)
print("Sample data generated and saved to 'hotel_bookings.csv'")
