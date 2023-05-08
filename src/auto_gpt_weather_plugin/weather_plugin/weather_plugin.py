import asyncio
import os

import python_weather

from python_weather import Client as WeatherClient


def get_client():
    if os.getenv("WEATHER_PLUGIN_UNITS", "metric") != "imperial":
        unit = python_weather.METRIC
    else:
        unit = python_weather.IMPERIAL

    client = WeatherClient(unit=unit)
    return client


async def get_weather_async(city: str):
    forecasts = ""
    client = get_client()
    data = await client.get(city)
    units = {
        "temp": "°F" if client.unit == python_weather.IMPERIAL else "°C",
        "precipitation": "inches" if client.unit == python_weather.IMPERIAL else "mm",
        "speed": "mph" if client.unit == python_weather.IMPERIAL else "km/h"
    }

    for forecast in data.forecasts:
        forecasts += format_forecast(forecast, units)

    return f"The weather in {city} is {data.current.description},\n" \
           f"the temperature is {data.current.temperature}{units['temp']} and feels like " \
           f"{data.current.feels_like}{units['temp']}, with a humidity of {data.current.humidity}% " \
           f"and {data.current.precipitation}{units['precipitation']} of precipitation.\n" \
           f"\n\nForecasts:\n\n{forecasts}"


def format_forecast(forecast, units):
    def get_rain(hourlies):
        chance = 0
        for hourly in hourlies:
            chance = max(chance, hourly.chances_of_rain)
        return chance

    result = f"Forecast for {forecast.date}:\n" \
             f"The Temperature is estimated to be between {forecast.lowest_temperature}{units['temp']} " \
             f"and {forecast.highest_temperature}{units['temp']}.\n" \
             f"The predicted chance of rain is {get_rain(forecast.hourly)}%\n" \
             f"Sunrise is at {forecast.astronomy.sun_rise} and sunset is at {forecast.astronomy.sun_set}\n\n"
    # commented out because it's too much text, and will crash your token limits
    #    result += "\nHourly forecasts\n"
    #    for hourly in forecast.hourly:
    #        result += f"For {hourly.time:%H:%M} o' clock the weather is expected to be {hourly.description}\n" \
    #                  f"the temperature is supposed to be  {hourly.temperature}{units['temp']}, " \
    #                  f"the chance of rain is supposed to be  {hourly.chances_of_rain}%, " \
    #                  f"the chance of snow is supposed to be  {hourly.chances_of_snow}%, " \
    #                  f"the predicted wind speed is {hourly.wind_speed}{units['speed']}\n\n "
    #    result += "\n\n\n\n"
    return result


def get_weather_for(city: str):
    try:
        result = asyncio.run(get_weather_async(city))
    except Exception as e:
        return f"Error: could not get weather: {e}"
    return result
