import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Debug print: Show status code and error message
        print("Error:", response.status_code, response.text)
        return None

def main():
    # Replace with your actual API key if you have one, otherwise follow steps below:
    API_KEY = "524067ca718d5ce38d11ff30657f5aa0"
    city = input("Enter a city name: ")
    weather_data = get_weather(city, API_KEY)
    
    if weather_data:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        
        print(f"\nCurrent weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather data. Please check the city name and your API key.")

if __name__ == "__main__":
    main()
