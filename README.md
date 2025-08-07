
# Weather-Responsive Clothing Advisor

An intelligent AI-powered clothing suggestion web app built using **Streamlit**. The application fetches **live weather data** and recommends appropriate clothing based on the **temperature** and **weather conditions** in Indian cities.

---

## Features

- Real-time weather data using [WeatherAPI](https://www.weatherapi.com/)
- Dynamic clothing suggestions based on live weather
- Interactive user interface with Streamlit
- Optimized for Indian cities such as Delhi, Mumbai, and Bangalore

---

## Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **API**: WeatherAPI  
- **Environment Management**: python-dotenv  
- **Others**: Git, Markdown

---

## Screenshot

The interface of the application when running locally:

![App Screenshot](screenshot.png)

---

## How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/sanyagupta31/weather-clothing-advisor.git
cd weather-clothing-advisor




### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # For Linux/Mac
venv\Scripts\activate          # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

* Create a `.env` file in the root directory
* Add your WeatherAPI key:

```env
WEATHER_API_KEY=your_actual_api_key
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📁 File Structure

```bash
weather-clothing-advisor/
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── .env                  # API key (not pushed to GitHub)
├── .gitignore            # Files to ignore in version control
└── README.md             # Project documentation
```

---

## ⚠️ Note

This app currently supports **only Indian cities**. Ensure your WeatherAPI key is valid and not expired. Visit [WeatherAPI](https://www.weatherapi.com/) to generate a free key.

---

## 🙌 Acknowledgments

* [Streamlit](https://streamlit.io/)
* [WeatherAPI](https://www.weatherapi.com/)
* Inspiration from everyday struggle of choosing the right outfit in unpredictable Indian weather 🌦️👕

---

## 📬 Contact

If you find this project helpful or have suggestions, feel free to reach out or open an issue!

```


