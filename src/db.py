import os
from supabase import create_client, Client
from dotenv import load_dotenv

#loading environment variables 
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if SUPABASE_URL and SUPABASE_KEY:
    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#create task
    def insert_record(day,temperature,category):
        data = {"data":day,"temperature":temperature,"category":category}
        return supabase.table("WeatherData").insert(data).execute()
    
    def fetch_records():
        return supabase.table("WeatherData").select("*").execute().data
    
    def update_record(record_id, day=None, temperature=None, category=None):
        data = {}
        if day: data["day"] = day
        if temperature is not None: data["temperature"] = temperature
        if category: data["category"] = category
        return supabase.table("WeatherData").update(data).eq("id", record_id).execute()
    
    def delete_record(record_id):
        return supabase.table("WeatherData").delete().eq("id", record_id).execute()
else:
    import sqlite3
    conn = sqlite3.connect("weather.db", check_same_thread=False)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS WeatherData(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 day TEXT, temperature REAL, category TEXT
                 )
                 """)
    conn.commit()
    def insert_record(day,temperature,category):
        conn.execute("INSERT INTO WeatherData (day, temperature, category) VALUES (?, ?, ?)", (day, temperature, category))
        conn.commit()
        return {"message": "Record inserted successfully"}
    def fetch_records():
        cur = conn.execute("SELECT * FROM WeatherData")
        return [dict(row) for row in cur.fetchall()]
    def update_record(record_id, day=None, temperature=None, category=None):
        fields = []
        values = []

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
        return {"message": f"Record {record_id} updated successfully"}

    def delete_record(record_id):
        conn.execute("DELETE FROM WeatherData WHERE id = ?", (record_id,))
        conn.commit()
        return {"message": f"Record {record_id} deleted successfully"}

