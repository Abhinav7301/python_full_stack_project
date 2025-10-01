# src/logic.py

"""
This file contains the business logic for the Weather Data Analysis project.
It handles:
- Categorizing days into Hot, Cold, Moderate
- Computing basic statistics (max, min, avg)
- Summarizing weekly weather data
- Provides CRUD operations by using db.py
"""

from src import db

# Thresholds for classifying temperatures
HOT_THRESHOLD = 35.0   # Above this → Hot
COLD_THRESHOLD = 28.0  # Below this → Cold


class TaskManager:
    """
    Acts as a bridge between frontend (Streamlit/FastAPI) and the database.
    Uses db.py functions internally for CRUD operations.
    """

    # ---------------------------
    # CRUD Operations
    # ---------------------------
    def create_record(self, day: str, temperature: float):
        """Insert a new record with automatic categorization."""
        category = categorize(temperature)
        return db.insert_record(day, temperature, category)

    def read_records(self):
        """Fetch all records and return with a summary."""
        records = db.fetch_records()
        return summarize_records(records)

    def update_record(self, record_id: int, day: str = None, temperature: float = None, category: str = None):
        """
        Update a record by id.
        If temperature changes and category not provided → recategorize automatically.
        """
        if temperature is not None and category is None:
            category = categorize(temperature)
        return db.update_record(record_id, day=day, temperature=temperature, category=category)

    def delete_record(self, record_id: int):
        """Delete a record by id."""
        return db.delete_record(record_id)


# ---------------------------
# Business Logic Functions
# ---------------------------

def categorize(temp: float) -> str:
    """Categorize a single temperature into Hot, Cold, or Moderate."""
    if temp > HOT_THRESHOLD:
        return "Hot"
    elif temp < COLD_THRESHOLD:
        return "Cold"
    else:
        return "Moderate"


def compute_stats(temps: list) -> dict:
    """Compute basic statistics from a list of temperatures."""
    if not temps:
        return {"max": None, "min": None, "avg": None}

    return {
        "max": max(temps),
        "min": min(temps),
        "avg": round(sum(temps) / len(temps), 2)
    }


def summarize_records(records: list) -> dict:
    """
    Summarize weather data from DB records.
    Input: list of dicts (each with day, temperature, category)
    Output: records + stats + category counts
    """
    if not records:
        return {"records": [], "stats": {}, "counts": {}}

    temps = [r["temperature"] for r in records]

    stats = compute_stats(temps)
    counts = {
        "Hot": sum(1 for r in records if r["category"] == "Hot"),
        "Cold": sum(1 for r in records if r["category"] == "Cold"),
        "Moderate": sum(1 for r in records if r["category"] == "Moderate"),
    }

    return {"records": records, "stats": stats, "counts": counts}
