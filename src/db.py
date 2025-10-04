import os
from dotenv import load_dotenv

# Load environment
load_dotenv()
USE_SUPABASE = os.getenv("USE_SUPABASE", "0") == "1"
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = None
if USE_SUPABASE and SUPABASE_URL and SUPABASE_KEY:
    try:
        from supabase import create_client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("[INFO] Using Supabase as database.")
    except Exception as e:
        print("[ERROR] Supabase client init failed:", e)
        supabase = None

if supabase:
    def insert_record(day, temperature, category):
        try:
            data = {"day": day, "temperature": temperature, "category": category}
            res = supabase.table("WeatherData").insert(data).execute()
            return {"message": "Inserted into Supabase", "data": res.data}
        except Exception as e:
            return {"error": str(e)}

    def fetch_records():
        try:
            res = supabase.table("WeatherData").select("*").execute()
            return res.data
        except Exception as e:
            return {"error": str(e)}

    def update_record(record_id, day=None, temperature=None, category=None):
        try:
            data = {}
            if day: data["day"] = day
            if temperature is not None: data["temperature"] = temperature
            if category: data["category"] = category
            res = supabase.table("WeatherData").update(data).eq("id", record_id).execute()
            return {"message": f"Record {record_id} updated", "data": res.data}
        except Exception as e:
            return {"error": str(e)}

    def delete_record(record_id):
        try:
            res = supabase.table("WeatherData").delete().eq("id", record_id).execute()
            return {"message": f"Record {record_id} deleted", "data": res.data}
        except Exception as e:
            return {"error": str(e)}

else:
    import sqlite3
    conn = sqlite3.connect("weather.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("""
    CREATE TABLE IF NOT EXISTS WeatherData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        temperature REAL,
        category TEXT
    )
    """)
    conn.commit()
    print("[INFO] Using SQLite as database (weather.db).")

    def insert_record(day, temperature, category):
        try:
            conn.execute("INSERT INTO WeatherData (day, temperature, category) VALUES (?, ?, ?)",
                         (day, temperature, category))
            conn.commit()
            return {"message": "Inserted into SQLite"}
        except Exception as e:
            return {"error": str(e)}

    def fetch_records():
        cur = conn.execute("SELECT * FROM WeatherData")
        return [dict(row) for row in cur.fetchall()]

    def update_record(record_id, day=None, temperature=None, category=None):
        fields, values = [], []
        if day:
            fields.append("day = ?")
            values.append(day)
        if temperature is not None:
            fields.append("temperature = ?")
            values.append(temperature)
        if category:
            fields.append("category = ?")
            values.append(category)

        if not fields:
            return {"error": "No fields to update"}

        values.append(record_id)
        query = f"UPDATE WeatherData SET {', '.join(fields)} WHERE id = ?"
        conn.execute(query, values)
        conn.commit()
        return {"message": f"Record {record_id} updated"}

    def delete_record(record_id):
        conn.execute("DELETE FROM WeatherData WHERE id = ?", (record_id,))
        conn.commit()
        return {"message": f"Record {record_id} deleted"}
