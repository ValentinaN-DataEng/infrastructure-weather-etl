from extract import extract_weather
from transform import transform_weather
from load import load_to_csv

def main():
    latitude = 4.7110
    longitude = -74.0721

    raw_data = extract_weather(latitude, longitude)
    clean_data = transform_weather(raw_data)
    load_to_csv(clean_data)

    print("Weather ETL pipeline executed successfully 🚀")

if __name__ == "__main__":
    main()
