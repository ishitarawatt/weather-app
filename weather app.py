import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("❌ City not found")
            return

        print(f"\n🌤 Weather in {city}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Condition: {data['weather'][0]['description']}")

    except requests.exceptions.RequestException:
        print("❌ Network error")

while True:
    city = input("\nEnter city name (or exit): ")
    if city.lower() == "exit":
        break
    get_weather(city)
