import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for OpenWeather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """Fetch weather data from OpenWeather API for a specific city."""
    try:
        request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = main["temp"]
            humidity = main["humidity"]

            print(f"City: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_desc}")
        else:
            print(f"City {city_name} not found!")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
