import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

# Function to fetch weather from WeatherAPI
def get_weather(city):
    # Always search in India
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},IN"

    try:
        response = requests.get(url)
        data = response.json()

        # Check for API errors
        if 'error' in data:
            st.error(f"API Error: {data['error']['message']}")
            return None, None

        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return temp, condition
    except Exception as e:
        st.error(f"Request failed: {e}")
        return None, None


# Suggest clothes based on temperature and condition
def suggest_clothing(temp, condition):
    condition = condition.lower()

    if "rain" in condition or "thunderstorm" in condition:
        if temp < 20:
            return "🌧️ Wear a raincoat and warm clothes + umbrella"
        else:
            return "🌂 Use umbrella and waterproof shoes"
    elif temp > 35:
        return "🕶️ Wear breathable cotton + sunglasses"
    elif 25 <= temp <= 35:
        return "👕 Wear light cotton clothes"
    elif 15 <= temp < 25:
        return "🧥 Wear full sleeves or a light sweater"
    else:
        return "🧣 Wear warm clothes, jacket, and scarf"

# Streamlit UI
st.set_page_config(page_title="Weather Clothing Advisor", page_icon="🌤️")
st.title("👗 Weather-Responsive Clothing Advisor")

city = st.text_input("Enter your city name", "")

if st.button("Get Advice"):
    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:
        temp, condition = get_weather(city)

        if temp is not None:
            st.success(f"**Current weather in {city.title()}**")
            st.markdown(f"- **Temperature**: {temp}°C")
            st.markdown(f"- **Condition**: {condition}")
            advice = suggest_clothing(temp, condition)
            st.markdown(f"### 🧥 Clothing Advice:")
            st.info(advice)
