from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_current_weather(city="Noida"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('OPENWEATHERMAP_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print()
    print("Hello, welcome to the weather app!")
    print()
    city = input("What city would you like to check the weather for? ")
    weather_data = get_current_weather(city)
    print()
    print("Here is the weather data:")
    pprint(weather_data)
