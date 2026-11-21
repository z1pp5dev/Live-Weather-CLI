
# Live Weather CLI

A command-line weather forecasting tool built in Python that fetches real-time meteorological conditions for any ZIP code. Powered by the [Open-Meteo Geocoding & Forecast APIs](https://open-meteo.com/), the script combines external JSON configuration, interactive user input with automatic fallback defaults, defensive network error handling, and color-coded terminal formatting via [Colorama](https://github.com/tartley/colorama).
## Features

* **Interactive Location Lookup & Config Fallback:** Prompts the user for a ZIP code at runtime and automatically falls back to a default location defined in `config.json` if left blank.
* **Two-Step Geocoding & Forecast Pipeline:** Dynamically resolves location queries into geographic coordinates (`latitude` and `longitude`) via Open-Meteo's Geocoding API before querying the live weather forecast endpoint.
* **Configurable Units & Metrics:** Driven by `config.json` to customize temperature units (`fahrenheit` / `celsius`), wind speed units (`mph` / `kmh`), and requested current weather metrics (`temperature_2m`, `apparent_temperature`, `precipitation_probability`, `cloud_cover`, `relative_humidity_2m`, and `wind_speed_10m`).
* **Styled Terminal Readout:** Uses `colorama` to frame the forecast report with clean headers and color-coded highlights for easy scanning.
* **Defensive Network Error Handling:** Gracefully catches `Timeout`, `ConnectionError`, and `HTTPError` exceptions alongside missing geocoding results without crashing.
## Prerequisites & Installation

1. Python 3.x installed on your local machine.

2. Clone the repository and navigate into the project directory:

   ```bash
   git clone https://github.com/z1pp5dev/live-weather-cli.git
cd live-weather-cli
```
    
## Create and activate a virtual environment:

   ```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
##  Install Required Dependencies:

```bash
pip install -r requirements.txt
```
## Run the weather script from your terminal:

```bash
python weather_fetcher_v2.py
```
1. When prompted (Please Enter Your ZIP code (Press ENTER to use defaults):), type a 5-digit ZIP code and press Enter—or press Enter immediately to use the fallback location in config.json.

2. The script will resolve the coordinates and display the formatted weather report directly in your terminal:

====================================
           WEATHER REPORT
====================================
Resolved '10451' to Coordinates: 40.1551, -75.888: New York City

Current Temperature in New York City, United States is: 54.2°F

Feels Like: 51.8°F

Chance of precipitation is: 10%

Today's cloud coverage is: 25%

Wind Speed is: 8.4MPH

Humidity: 48%
## Error Handling

This script uses `try`/`except` blocks and safe dictionary lookups to handle unexpected network or lookup conditions without raising an unhandled traceback:

* **Timeouts (`requests.exceptions.Timeout`):** Alerts the user if a request to the geocoding or forecast API takes longer than the configured timeout.
* **Connection Errors (`requests.exceptions.ConnectionError`):** Catches network or connectivity failures and prints a friendly retry message.
* **HTTP Errors (`requests.exceptions.HTTPError`):** Triggered via `response.raise_for_status()` when an endpoint responds with an HTTP error status.
* **Unmatched Locations:** Verifies that geocoding results are present before accessing coordinates or weather metrics, and falls back to `config.json` when no ZIP code is entered.
## 🚀 About Me
I'm am a independent backend devleoper, looking to create and share helpful and meaningfull projects and programs for all to use!
## Support

For support, email z1pp5.dev02@gmail.com


