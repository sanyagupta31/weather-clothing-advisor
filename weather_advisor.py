import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
import streamlit.components.v1 as components

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

# --- Functions ---

# Function to automatically refresh the page
def auto_refresh(interval_seconds=7200):
    """Injects a meta tag to auto-refresh the page."""
    components.html(
        f"""
        <meta http-equiv="refresh" content="{interval_seconds}">
        """,
        height=0,
    )

# Function to fetch current and forecast data from WeatherAPI
def fetch_weather_data(city):
    """Fetches 7-day weather forecast for a given Indian city."""
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": f"{city},IN",  # Search within India
        "days": 7,
        "aqi": "no",
        "alerts": "no"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        if 'error' in data:
            st.error(f"API Error: {data['error']['message']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return None

# Rule-based logic for clothing suggestions
def suggest_clothing(temp, condition):
    """Suggests clothing based on temperature and weather condition."""
    condition = condition.lower()
    if "rain" in condition or "thunder" in condition:
        if temp < 20:
            return "Wear a raincoat over warm clothes and carry an umbrella"
        else:
            return "Use waterproof shoes and carry an umbrella"
    elif temp > 35:
        return "Wear breathable cotton clothes and sunglasses"
    elif 25 <= temp <= 35:
        return "Wear light cotton clothes"
    elif 15 <= temp < 25:
        return "Wear full sleeves or a light jacket"
    else:  # temp < 15
        return "Wear a warm jacket and a scarf"

# Fallback sample data for testing
def get_sample_data():
    """Provides a sample DataFrame for offline testing."""
    return pd.DataFrame({
        "Date": ["2025-08-07", "2025-08-08"],
        "City": ["SampleCity", "SampleCity"],
        "Temp (°C)": [16, 34],
        "Condition": ["Rainy", "Sunny"],
        "Clothing Advice": ["Wear full sleeves or a light jacket", "Wear light cotton clothes"]
    })

# --- Streamlit UI ---

st.set_page_config(page_title="Weather Clothing Advisor")

# Call the auto-refresh function
auto_refresh(interval_seconds=7200)

st.title("Weather-Responsive Clothing Advisor")

use_sample = st.checkbox("Use Sample Data (for testing without API key)")
city_input = st.text_input("Enter Indian city name", value="Delhi")

if st.button("Get Clothing Advice"):
    if use_sample:
        df = get_sample_data()
        st.success("Sample Data Loaded.")
        st.dataframe(df)
        st.download_button("Download as CSV", df.to_csv(index=False), "sample_clothing_advice.csv", "text/csv")
    else:
        if not api_key:
            st.error("WEATHER_API_KEY is not set. Please add it to your .env file.")
        elif not city_input.strip():
            st.warning("Please enter a city name.")
        else:
            data = fetch_weather_data(city_input)

            if data:
                st.header("Advisory Summary")

                # --- Expected Output Section ---
                # Today's Summary
                current = data['current']
                today_advice = suggest_clothing(current['temp_c'], current['condition']['text'])
                st.info(f"{city_input.title()} Today: {current['temp_c']}°C - {today_advice}")

                # Tomorrow's Summary
                if len(data['forecast']['forecastday']) > 1:
                    tomorrow = data['forecast']['forecastday'][1]['day']
                    tomorrow_advice = suggest_clothing(tomorrow['avgtemp_c'], tomorrow['condition']['text'])
                    st.info(f"{city_input.title()} Tomorrow: {tomorrow['avgtemp_c']}°C and {tomorrow['condition']['text']} -- {tomorrow_advice}")

                # --- Weekly Plan Section ---
                st.header("Weekly Plan Builder")
                
                forecast_days = data['forecast']['forecastday']
                rows = []
                for day in forecast_days:
                    date = day['date']
                    temp = day['day']['avgtemp_c']
                    condition = day['day']['condition']['text']
                    advice = suggest_clothing(temp, condition)
                    rows.append([date, city_input.title(), temp, condition, advice])

                df = pd.DataFrame(rows, columns=["Date", "City", "Avg Temp (°C)", "Condition", "Clothing Advice"])
                
                st.dataframe(df)
                st.download_button(
                    label="Download Weekly Plan as CSV",
                    data=df.to_csv(index=False),
                    file_name=f"{city_input.lower()}_weekly_advice.csv",
                    mime="text/csv"
                )

st.caption("This page automatically updates the weather data every 2 hours.")