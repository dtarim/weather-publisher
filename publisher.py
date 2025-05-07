import json
import subprocess
import time
import requests

SERVER_URL = "http://192.168.178.86:5050/update_weather"

def get_weather(city):
    result = subprocess.getoutput(f"./get_weather.sh '{city}'")
    return result.strip()

def main():
    with open ("cities.json", "r") as f:
        cities_data = json.load(f)
    
    weather_payload = {}
    for continent, cities in cities_data.items():
        for city in cities:
            temp = get_weather(city)
            weather_payload[city] = temp
            time.sleep(1)  # wtte.in fazla istekten banliyor

    #posting data to server
    try:
        response = requests.post(SERVER_URL, json=weather_payload)
        print(f"Server response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error posting data to server: {e}")

if __name__ == "__main__":
    main()