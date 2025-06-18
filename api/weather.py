import requests


def get_weather(city):
    try:
        city = city.replace(" ", "-")
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        text = response.text.strip()

        if response.status_code == 200:
            if "Unknown location" in text or len(text) < 10:
                return "City not found. Please try another one."
            return text
        else:
            return f"Error {response.status_code}: Unable to retrieve weather data at the moment."
    except Exception as e:
        return f"Error: {e}"
    