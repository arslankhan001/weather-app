import requests
from datetime import datetime
#importing requests module to make api requests to get the weather data
#importing datetime module to convert the date and time into more readable format.

#function to fetch the weather data from openweathermap using the city name
def get_weather_by_city(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    # You can change units to imperial if you prefer Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error:", data["message"])
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None

#function to fetch the weather from openweathermap using the zip code of that location
def get_weather_by_zip(api_key, zip_code, country_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"zip": f"{zip_code},{country_code}", "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error:", data["message"])
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None


#function to get 5 day forecast for that location
def get_5_day_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error:", data["message"])
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None

#function to diplay the current weather data
def display_current_weather(weather_data):
    if weather_data:
        print(f"Current Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Sunrise: {timestamp_to_time(weather_data['sys']['sunrise'])}")
        #timestamp to time turns it into a readable format YYYY-MM-DD HR:MN:SS
        print(f"Sunset: {timestamp_to_time(weather_data['sys']['sunset'])}")
    else:
        print("Weather data not available.")

#function to display 5 day forecast
def display_5_day_forecast(forecast_data):
    if forecast_data:
        print("5-Day Forecast:")
        for entry in forecast_data['list']:
            timestamp = entry['dt']
            date = timestamp_to_time(timestamp, format='%Y-%m-%d %H:%M:%S')
            temperature = entry['main']['temp']
            description = entry['weather'][0]['description']

            print(f"{date}: Temperature: {temperature}°C, Description: {description}")

    else:
        print("Forecast data not available.")

def timestamp_to_time(timestamp, format='%Y-%m-%d %H:%M:%S'):
    return datetime.utcfromtimestamp(timestamp).strftime(format)

if __name__ == "__main__":
    #personal api key obained from openweathermap
    # please use your personalised api key from openweathermap
    # api_key = "3dc860e03ea9c272cd690bdd132ef09d"

    while True:
        location_type = input("Enter 'city' or 'zip' to specify location type (or 'exit' to quit): ")

        if location_type.lower() == 'exit':
            print("Exiting the weather app. Goodbye!")
            break

        if location_type == "city":
            city = input("Enter the city name: ")
            weather_data = get_weather_by_city(api_key, city)
            forecast_data = get_5_day_forecast(api_key, city)
        elif location_type == "zip":
            zip_code = input("Enter the zip code: ")
            country_code = input("Enter the country code (e.g., US): ")
            weather_data = get_weather_by_zip(api_key, zip_code, country_code)
            forecast_data = get_5_day_forecast(api_key, f"{zip_code},{country_code}")
        else:
            print("Invalid location type. Please enter 'city' or 'zip'.")

        display_current_weather(weather_data)
        display_5_day_forecast(forecast_data)