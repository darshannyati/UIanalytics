from datetime import datetime, timedelta
import random
import json

# Sample data
languages = ["English", "Spanish", "French", "German", "Chinese", "Hindi"]
platforms = ["Android", "iOS"]
genders = ["Male", "Female"]
countries = ["USA", "Canada", "UK", "Australia", "India"]
ui = ["A", "B"]

start_date = datetime(2023, 1, 1)

users = []

for i in range(1, 501):
    # Random date within 2023
    random_days = random.randint(0, 364)
    date = start_date + timedelta(days=random_days)

    # Random time between 00:00 and 23:59
    random_minutes = random.randint(0, 1439)
    time = timedelta(minutes=random_minutes)

    full_datetime = date + time

    user = {
        "id": i,
        "language": random.choice(languages),
        "platform": random.choice(platforms),
        "gender": random.choice(genders),
        "country": random.choice(countries),
        "success": random.choice([True, False]),
        "ui": random.choice(ui),
        "timestamp": full_datetime.strftime("%Y-%m-%d %H:%M:%S")
    }
    users.append(user)

# Save to JSON
with open("synthetic_users_with_time.json", "w") as f:
    json.dump(users, f, indent=4)

print("Synthetic data with time saved.")
