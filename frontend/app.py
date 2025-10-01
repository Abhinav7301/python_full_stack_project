# frontend/app.py
import streamlit as st
import requests

# -----------------------------
# API base URL
# -----------------------------
API_URL = "http://127.0.0.1:8000"

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Weather Data Analyzer", layout="wide")
st.title("🌤️ Weather Data Analyzer")
st.write("Manage and analyze weekly temperature data.")


# -----------------------------
# Helper functions
# -----------------------------
def fetch_records():
    res = requests.get(f"{API_URL}/weather")
    if res.status_code == 200:
        return res.json()
    else:
        st.error(f"Error fetching records: {res.text}")
        return {"records": [], "stats": {}, "counts": {}}


def create_record(day, temperature):
    res = requests.post(f"{API_URL}/weather", json={"day": day, "temperature": temperature})
    if res.status_code == 200:
        st.success("✅ Record created successfully")
    else:
        st.error(f"Error: {res.text}")


def update_record(record_id, day=None, temperature=None, category=None):
    payload = {}
    if day:
        payload["day"] = day
    if temperature:
        payload["temperature"] = temperature
    if category:
        payload["category"] = category

    res = requests.put(f"{API_URL}/weather/{record_id}", json=payload)
    if res.status_code == 200:
        st.success(f"✅ Record {record_id} updated")
    else:
        st.error(f"Error: {res.text}")


def delete_record(record_id):
    res = requests.delete(f"{API_URL}/weather/{record_id}")
    if res.status_code == 200:
        st.success(f"🗑️ Record {record_id} deleted")
    else:
        st.error(f"Error: {res.text}")


# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Record", "📋 View Records", "✏️ Update Record", "🗑️ Delete Record"])

# --- Add Record ---
with tab1:
    st.subheader("Add New Weather Record")
    day = st.text_input("Day", placeholder="e.g., Mon")
    temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, step=0.5)

    if st.button("Add Record"):
        if day and temperature is not None:
            create_record(day, temperature)
        else:
            st.warning("Please enter both Day and Temperature")

# --- View Records ---
with tab2:
    st.subheader("Weekly Records and Summary")
    data = fetch_records()
    records = data.get("records", [])
    stats = data.get("stats", {})
    counts = data.get("counts", {})

    if records:
        st.table(records)

        st.markdown("### 📊 Statistics")
        st.json(stats)

        st.markdown("### 📌 Category Counts")
        st.json(counts)
    else:
        st.info("No records found yet.")

# --- Update Record ---
with tab3:
    st.subheader("Update Weather Record")
    rec_id = st.number_input("Record ID", min_value=1, step=1)
    new_day = st.text_input("New Day (optional)")
    new_temp = st.number_input("New Temperature (optional)", min_value=-50.0, max_value=60.0, step=0.5, value=0.0)
    update_cat = st.selectbox("Category (optional)", ["", "Hot", "Cold", "Moderate"])

    if st.button("Update Record"):
        payload = {}
        if new_day:
            payload["day"] = new_day
        if new_temp != 0.0:
            payload["temperature"] = new_temp
        if update_cat:
            payload["category"] = update_cat

        if payload:
            update_record(rec_id, **payload)
        else:
            st.warning("Please provide at least one field to update.")

# --- Delete Record ---
with tab4:
    st.subheader("Delete Weather Record")
    del_id = st.number_input("Record ID to delete", min_value=1, step=1)

    if st.button("Delete Record"):
        delete_record(del_id)
