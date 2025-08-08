

````markdown
# Weather-Responsive Clothing Advisor

An intelligent web app built with Python and Streamlit that provides clothing recommendations based on live weather data for any city in India. The application fetches real-time temperature and weather conditions to help you decide what to wear.

---

## ✨ Features

-   **Live Weather Data**: Fetches real-time weather information for any Indian city using the WeatherAPI.
-   **Rule-Based Recommendations**: Suggests appropriate clothing based on temperature and conditions (e.g., sunny, rainy, cold).
-   **7-Day Forecast**: Displays a weekly weather forecast and clothing plan.
-   **Export to CSV**: Allows users to download the weekly plan for offline access.
-   **Automatic Refresh**: The weather data automatically updates every 2 hours to provide the most current advice.
-   **Clean User Interface**: A simple, fast, and icon-free interface built with Streamlit.

---

## 🛠️ Tech Stack

-   **Core Language**: Python 3.8+
-   **Web Framework**: Streamlit
-   **Data Handling**: Pandas
-   **API Communication**: Requests
-   **Environment Management**: python-dotenv
-   **Version Control**: Git & GitHub

---

## 📸 Screenshot

The interface of the application when running locally:

![App Screenshot](screenshot.png)

---

## 🚀 How to Run the Project Locally

### Prerequisites

-   [Python 3.8](https://www.python.org/downloads/) or higher
-   [Git](https://git-scm.com/downloads/)

### 1. Clone the Repository

Clone the repository to your local machine. Remember to replace `your-username/your-repository-name` with your actual GitHub details.
```bash
git clone [https://github.com/sanyagupta31/weather-clothing-advisor.git](https://github.com/sanyagupta31/weather-clothing-advisor.git)
cd weather-clothing-advisor
````

### 2\. Create and Activate a Virtual Environment

```bash
# For Linux/Mac
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3\. Install Dependencies

Install all the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Set Up Your API Key

  - Create a file named `.env` in the root directory of the project.
  - Sign up on [WeatherAPI](https://www.weatherapi.com/) to get your free API key.
  - Add your API key to the `.env` file as shown below:

<!-- end list -->

```env
WEATHER_API_KEY=your_actual_api_key_here
```

### 5\. Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your default web browser.

-----

## 📁 File Structure

```
weather-clothing-advisor/
├── app.py              # Main Streamlit application script
├── requirements.txt    # Project dependencies
├── .env                # For storing the API key (not tracked by Git)
├── .gitignore          # Files and directories to be ignored by Git
└── README.md           # Project documentation
```

-----

## ⚠️ Note

  - This application is configured to search for cities **only within India**.
  - Ensure your `WEATHER_API_KEY` is valid and has not expired.

-----

## 🙌 Acknowledgments & Contribution

  - This project was inspired by the daily challenge of choosing an outfit for India's unpredictable weather.
  - A big thanks to [Streamlit](https://streamlit.io/) and [WeatherAPI](https://www.weatherapi.com/) for their excellent tools.

Contributions are welcome\! If you have suggestions or want to improve the app, please feel free to open an issue or submit a pull request.

```
```