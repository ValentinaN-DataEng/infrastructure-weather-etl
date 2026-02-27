import requests

def extract_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API")
