import requests

def get_weather_data(city):
    """Fetches weather data for a specific city using WeatherAPI."""
    api_key = "82e11a3bd0804a5994480502252907"  # Ideally, store this in an environment variable
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise exception for bad HTTP status codes
        data = response.json()

        if 'error' not in data:
            weather = data['current']['condition']['text']
            temp_c = data['current']['temp_c']
            print(f"Weather: {weather}, Temperature: {temp_c}°C")

            if "Heavy rain" in weather:
                print("Weather condition is heavy rain.")
            else:
                print("Weather condition is not heavy rain.")
        else:
            print(f"Error fetching data for {city}: {data['error']['message']}")

    except requests.RequestException as e:
        print(f"Network error: {e}")




get_weather_data('London')

