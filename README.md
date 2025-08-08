

````markdown
🌦️ **Weather-Responsive Clothing Advisor**

An AI-powered, rule-based web application built with Python and Streamlit that helps you decide what to wear based on live weather conditions in any Indian city.  
It fetches real-time temperature and weather conditions from the WeatherAPI, and then suggests ideal outfits for the day or week.

---

**✨ Features**

- 📡 **Live Weather Data** – Get up-to-date weather information for any Indian city using [WeatherAPI](https://www.weatherapi.com/).
- 👕 **Rule-Based Recommendations** – Suggests clothing based on temperature and weather conditions (e.g., sunny, rainy, cold).
- 📅 **7-Day Forecast** – View a complete weekly weather and clothing plan.
- 💾 **Export to CSV** – Download the weekly clothing plan for offline use.
- ⏱️ **Automatic Refresh** – Weather data updates automatically every 2 hours for accuracy.
- 🖥️ **Clean UI** – Minimal, responsive, and easy-to-use interface built with Streamlit.

---

**🛠️ Tech Stack**

| Component         | Technology Used |
|-------------------|-----------------|
| Language          | Python 3.8+     |
| Framework         | Streamlit       |
| Data Handling     | Pandas          |
| API Requests      | Requests        |
| Env Management    | python-dotenv   |
| Version Control   | Git & GitHub    |

---

**📸 Screenshot**

Example of the application interface when running locally:

![App Screenshot](screenshot.png)

---

**🚀 Getting Started**

**Prerequisites**
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)

**1. Clone the Repository**
```bash
git clone https://github.com/sanyagupta31/weather-clothing-advisor.git
cd weather-clothing-advisor
````

**2. Create and Activate a Virtual Environment**

```bash
# For Linux/Mac
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Set Up Your API Key**

1. Create a `.env` file in the project root.
2. Get your free API key from [WeatherAPI](https://www.weatherapi.com/).
3. Add the key to `.env`:

```env
WEATHER_API_KEY=your_actual_api_key_here
```

**5. Run the App**

```bash
streamlit run app.py
```

The application will open in your default browser.

---

**📂 Project Structure**

```
weather-clothing-advisor/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API key storage (ignored by Git)
├── .gitignore          # Ignore unnecessary files
└── README.md           # Project documentation
```

---

**⚠️ Notes**

* The app is designed to fetch weather for **Indian cities only**.
* Make sure your WeatherAPI key is **active and valid**.

---

**🙌 Acknowledgments & Contributions**

* Inspired by the challenge of choosing outfits for India’s unpredictable weather.
* Thanks to [Streamlit](https://streamlit.io/) and [WeatherAPI](https://www.weatherapi.com/) for their amazing tools.

💡 Want to contribute? Fork the repo, create a branch, make changes, and submit a pull request. Suggestions are always welcome!

```

---


