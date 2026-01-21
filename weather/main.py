#weather application
import requests

API_KEY = "d7f8bde29e65469e7376c69a954448c0"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(location, unit_type):
    parameters = {
        "q": location,
        "appid": API_KEY,
        "units": unit_type
    }

    response = requests.get(WEATHER_ENDPOINT, params=parameters)

    if response.status_code != 200:
        return None

    weather_json = response.json()

    result = {
        "city": weather_json["name"],
        "temp": weather_json["main"]["temp"],
        "humidity": weather_json["main"]["humidity"],
        "description": weather_json["weather"][0]["description"]
    }

    return result


def run_weather_app():
    print("\n=== Weather Information System ===")

    user_location = input("Enter city name or ZIP code: ").strip()

    unit_choice = input("Choose temperature unit (C/F): ").strip().upper()
    units = "metric" if unit_choice == "C" else "imperial"
    symbol = "°C" if units == "metric" else "°F"

    weather = fetch_weather_data(user_location, units)

    if weather is None:
        print("\n Unable to retrieve weather data.")
        print("Please check the location or internet connection.")
        return

    print("\n🌤 Current Weather Report")
    print("----------------------------")
    print(f"Location   : {weather['city']}")
    print(f"Temperature: {weather['temp']}{symbol}")
    print(f"Humidity   : {weather['humidity']}%")
    print(f"Condition  : {weather['description'].capitalize()}")


run_weather_app()
