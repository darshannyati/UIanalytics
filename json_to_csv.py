import json
import csv

# Load JSON data
with open("synthetic_users_with_time.json", "r") as json_file:
    data = json.load(json_file)

# Extract keys from the first record to use as column headers
keys = data[0].keys()

# Write to CSV
with open("synthetic_users_with_time.csv", "w", newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

print("Converted JSON to CSV: synthetic_users_with_time.csv")
