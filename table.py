import json
import sqlite3

# Load JSON data
with open("synthetic_users_with_time.json", "r") as f:
    users = json.load(f)

# Connect to SQLite (it will create a new file if it doesn't exist)
conn = sqlite3.connect("synthetic_users.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        language TEXT,
        platform TEXT,
        gender TEXT,
        city TEXT,
        state TEXT,
        country TEXT,
        success BOOLEAN,
        ui TEXT,
        timestamp TEXT
    )
""")

# Insert data into table
for user in users:
    cursor.execute("""
        INSERT INTO users (id, language, platform, gender, city, state, country, success, ui, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user["id"],
        user["language"],
        user["platform"],
        user["gender"],
        user["city"],
        user["state"],
        user["country"],
        user["success"],
        user["ui"],
        user["timestamp"]
    ))

# Commit and close
conn.commit()
conn.close()

print("Data inserted into SQLite database: synthetic_users.db")
