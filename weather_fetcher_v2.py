#Layer 1 Imports
import json
import requests
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Layer 2 Configuration Settings
'''Load in configuration settings safely from disk'''
with open("config.json", 'r') as f:
  config = json.load(f)

#Pass Params from config file
'''Load in the url from config'''
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
user_zip = input("Please Enter Your ZIP code (Press ENTER to use defaults): ").strip()
divider = "=" * 36
title = "WEATHER REPORT".center(36)

if user_zip == "":
  location_query = config["location_search"]
elif len(user_zip) >= 5:
  location_query = user_zip
else:
 location_query = config['location_search']

geo_params = {"name": location_query, "count": 1}
# params = {
#     "latitude": config['default_latitude'],
#     "longitude": config['default_longitude'],
#     "current_weather": True,
#     "temperature_unit": config['temp_unit'],
# }

#Safe error handling / set response variable
try:
 geo_response = requests.get(geo_url, params=geo_params, timeout=5)
 geo_response.raise_for_status()
 geo_data = geo_response.json()
#Conditionals
 if "results" in geo_data and len(geo_data["results"]) > 0:
    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    place_name = location.get("name", config["location_search"])
    country = location.get("country", "")

    print(f"{Fore.YELLOW}Resolved '{location_query}' to Coordinates: {lat}, {lon}: {Style.BRIGHT}{Fore.WHITE}{place_name}{Style.RESET_ALL}")

#Step 2: Use resolved cords to fetch the weather forecast
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
            "latitude": lat,
            "longitude": lon,
           # "current_weather": True,
            "current": config["current_metrics"],
            "temperature_unit": config["temp_unit"],
            "wind_speed_unit": config["wind_speed_unit"]
   
}

    response = requests.get(weather_url, params=weather_params, timeout=5)
    response.raise_for_status()

    if response.status_code == 200:
         weather_data = response.json()
         current = weather_data.get("current", {})

         temp = current.get("temperature_2m")
         feels_like = current.get("apparent_temperature")
         precip_chance = current.get("precipitation_probability")
         cloud_cover = current.get("cloud_cover")
         humidity = current.get("relative_humidity_2m")
         wind_speed = current.get("wind_speed_10m")

         unit = (
        "°F" if config["temp_unit"].lower() == "fahrenheit" else "°C"
     )

         print(f"{Fore.CYAN}{Style.BRIGHT}{title}")
         print(f"{Fore.CYAN}{Style.BRIGHT}{divider}")
         print(f"{Fore.BLUE}Current Temperature in {place_name}, {country} is: {Style.BRIGHT}{Fore.WHITE}{temp}{unit}{Style.RESET_ALL}")
         print(f"{Fore.BLUE}Feels Like: {Style.BRIGHT}{Fore.WHITE}{feels_like}{unit}{Style.RESET_ALL}")
         print(f"{Fore.BLUE}Chance of precipitation is: {Style.BRIGHT}{Fore.WHITE}{precip_chance}%{Style.RESET_ALL}")
         print(f"{Fore.BLUE}Today's cloud coverage is: {Style.BRIGHT}{Fore.WHITE}{cloud_cover}%{Style.RESET_ALL}")
         print(f"{Fore.BLUE}Wind Speed is: {Style.BRIGHT}{Fore.WHITE}{wind_speed}MPH{Style.RESET_ALL}")
         print(f"{Fore.BLUE}Humidity: {Style.BRIGHT}{Fore.WHITE}{humidity}%{Style.RESET_ALL}")
 else:
    print(f"{Fore.RED}Could not find coordinates for: {config['location_search']}{Style.RESET_ALL}")
     
#Catches common errors and clearly states them without crashing script
except requests.exceptions.Timeout:
   print(Fore.RED + "Connection Timed Out!")
except requests.exceptions.ConnectionError:
   print(Fore.RED + "Connection Failed! Please check your internet connection...")
except requests.exceptions.HTTPError as err:
   print(f"{Fore.RED} HTTP Error occurred: {err}")