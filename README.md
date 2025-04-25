
# 📊 Paywall UI Analytics: An End-to-End A/B Testing and Analytics Project

This project simulates and analyzes user behavior on different paywall UIs (**UI A** and **UI B**) to determine which version performs better in terms of user conversions and success rate.

It includes synthetic data generation, API development using FastAPI, database storage using SQLite, JSON to CSV conversion, and interactive data visualization with Power BI.

---

## 🧠 Project Overview

- Simulates real-world paywall interactions using synthetic data
- Tracks user demographics, platform, UI version, and success status
- Differentiates between two paywall UI versions (A/B Testing)
- Exposes endpoints for logging and updating interaction outcomes
- Converts data to CSV for easier visualization
- Visualizes results in an interactive Power BI dashboard

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `main.py` | FastAPI application with API endpoints |
| `models.py` | SQLModel schema and database configuration |
| `table.py` | Script to insert data into SQLite database |
| `synthetic_data.py` | Generates synthetic user interaction data |
| `json_to_csv.py` | Converts JSON logs to CSV format |
| `synthetic_users_with_time.csv` | Final cleaned dataset used in Power BI |
| `report.pbix` | Power BI dashboard file |
| `Screenshot 2025-04-17 145510.png` | Power BI report snapshot |
| `README.md` | Project documentation |

---

## 🧰 Technologies Used

- **Python**
- **FastAPI**
- **SQLModel + SQLite**
- **Power BI**
- **Postman**
- **Pandas**

---

## 🔧 Setup Instructions

### 1️⃣ Install Requirements

```bash
pip install fastapi uvicorn sqlmodel sqlalchemy pandas
```

---

### 2️⃣ Run the API Server

```bash
uvicorn main:app --reload
```

Server will be available at: `http://127.0.0.1:8000`

---

### 3️⃣ Generate Synthetic Data

```bash
python synthetic_data.py
```

This creates randomized records with features like:
- Language, Country, Gender
- Platform (iOS/Android)
- Assigned UI version (A/B)
- Interaction timestamp and success status

---

### 4️⃣ Store Data in SQLite

```bash
python table.py
```

Saves user interactions into `sqlite.db`.

---

### 5️⃣ Convert JSON to CSV

If you're using the synthetic JSON data directly:

```bash
python json_to_csv.py
```

This converts the generated `synthetic_users_with_time.json` into a clean, tabular `synthetic_users_with_time.csv`, ready for use in Power BI.

---

## 🔌 API Endpoints

### `GET /info/`

Simulates a user interaction and returns a unique record ID and assigned UI version.

**Parameters:**
- `id`, `language`, `platform`, `gender`, `city`, `state`, `country`

**Example Request:**
```bash
curl "http://127.0.0.1:8000/info/?id=1&language=English&platform=iOS&gender=Male&city=Mumbai&state=Maharashtra&country=India"
```

---

### `POST /update-success/{rid}`

Marks a user interaction (by record ID) as successful.

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/update-success/123"
```

---

## 📈 Power BI Dashboard

The Power BI report provides insights into user interactions and performance of each UI version.

📂 File: `report.pbix`  
📷 Snapshot:  
![Power BI Dashboard](./Screenshot%202025-04-17%20145510.png)

---

### Dashboard Contents

#### ✅ KPI Cards
- **Total Users**
- **Successful Payments**
- **Success Rate**

#### 📊 Charts
- **Success Rate by Time Slot**
- **Success Rate by Gender**
- **Success Rate by Platform**

#### 🎛 Slicers
- **Country**
- **Language**
- **UI Version (A/B)**
- **Gender**

Use these interactive filters to analyze user behavior across different segments.

---

## 📌 Use Cases

- A/B testing for UI optimization
- Interactive analytics using Power BI
- Real-time API-based tracking simulation
- Full pipeline from data collection to insights

---

## 👨‍💻 Author

**Darshan Nyati**  
Final Year Computer Science Student

---
