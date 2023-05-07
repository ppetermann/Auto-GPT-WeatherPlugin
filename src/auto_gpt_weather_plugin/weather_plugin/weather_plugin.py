import asyncio
import os

import python_weather

from python_weather import Client as WeatherClient


def get_client():
    unitIn = os.getenv("WEATHER_PLUGIN_UNITS", "metric")

    if unitIn != "imperial":
        unit = python_weather.METRIC
    else:
        unit = python_weather.IMPERIAL

    client = WeatherClient(unit=unit)
    return client


async def get_weather_async(city: str):
    client = get_client()
    data = await client.get(city)
    tempunit = "°F" if client.unit == python_weather.IMPERIAL else "°C"
    percunit = "mm" if client.unit == python_weather.IMPERIAL else "inches"

    return f"The weather in {city} is {data.current.description},\n" \
           f"the temperature is {data.current.temperature}{tempunit} and feels like " \
           f"{data.current.feels_like}{tempunit}, with a humidity of {data.current.humidity}% " \
           f"and {data.current.precipitation}{percunit} of precipitation."


def get_weather_for(city: str):
    try:
        result = asyncio.run(get_weather_async(city))
        print(result)
    except Exception as e:
        return f"Error: could not get weather: {e}"
    return result
