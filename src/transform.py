def transform_weather(raw_data):
    current = raw_data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "winddirection": current["winddirection"],
        "time": current["time"]
    }
