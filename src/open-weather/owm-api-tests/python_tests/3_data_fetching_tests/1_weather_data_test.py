#!/usr/bin/env python3
# ============================================================================
"""
owm-api-test.

A set of tests that fetch wether data from API and validate it
"""
# ============================================================================

import requests


def test_collect_weather_data_and_validate():
    location_name = "Oxford"
    api_key = "c3c4ac2ce943d99aa52f886665b95bcf"

    try:
        url = "https://api.openweathermap.org/data/2.5/"\
            "weather?q={}&units=metric&appid={}".format(location_name, api_key)
        r = requests.get(url)
        weather = r.json()

        code = str(weather['cod'])
        print(code)
        city = str(weather['name'])
        country = weather['sys']['country']
        temp = weather['main']['temp']
        print(temp, "C", city, country)

        # For a successful API call we should have the correct city and country
        assert city == location_name and country == weather['sys']['country'],\
            "Unable to fetch data for {}".format(location_name)

    except requests.ConnectionError:
        print("Failed to establish a new connection: [Errno 11001]")
