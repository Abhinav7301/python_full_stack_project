#src/logic.py

from src.db import DatabaseManager

class TaskManager:
        """
        Acts as a bridge b.w frontend (streamlit/FASTAPI) and the database.
        """
        def __init__(self):
            self.db = DatabaseManager()
"""
This file contains the business logic for the Weather Data Analysis project.
It handles:
- Categorizing days into Hot, Cold, Moderate
- Computing basic statistics (max, min, avg)
- Summarizing weekly weather data
"""

# Thresholds for classifying temperatures
HOT_THRESHOLD = 35.0   # Above this → Hot
COLD_THRESHOLD = 28.0  # Below this → Cold


def categorize(temp: float) -> str:
    """
    Categorize a single temperature into Hot, Cold, or Moderate.
    """
    if temp > HOT_THRESHOLD:
        return "Hot"
    elif temp < COLD_THRESHOLD:
        return "Cold"
    else:
        return "Moderate"


def compute_stats(temps: list) -> dict:
    """
    Compute basic statistics from a list of temperatures.
    Returns max, min, and average.
    """
    if not temps:
        return {"max": None, "min": None, "avg": None}

    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = round(sum(temps) / len(temps), 2)

    return {
        "max": max_temp,
        "min": min_temp,
        "avg": avg_temp
    }


def summarize(days: list, temps: list) -> dict:
    """
    Summarize weekly weather:
    - day-wise records with categories
    - overall statistics
    - counts of Hot/Cold/Moderate days
    """
    if len(days) != len(temps):
        raise ValueError("Days and temperatures must have the same length")

    records = []
    categories = []

    for d, t in zip(days, temps):
        cat = categorize(t)
        categories.append(cat)
        records.append({"day": d, "temperature": t, "category": cat})

    stats = compute_stats(temps)

    counts = {
        "Hot": categories.count("Hot"),
        "Cold": categories.count("Cold"),
        "Moderate": categories.count("Moderate")
    }

    return {
        "records": records,
        "stats": stats,
        "counts": counts
    }

    