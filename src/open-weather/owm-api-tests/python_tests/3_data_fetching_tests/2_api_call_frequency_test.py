#!/usr/bin/env python3
# ============================================================================
"""
API frequency Test.

This test calls the OWM API 5 times in five seconds. If everything goes, fine
the resulting frequency should be 1 Hz(although passing the test will not show
the output frequency)

"""
# ============================================================================

import time
import requests


def test_api_frequency():

    location_name = 'Oxford'
    api_key = "c3c4ac2ce943d99aa52f886665b95bcf"

    starttime = time.time()
    timer = 0
    api_frequency_count = 0

    try:
        url = "https://api.openweathermap.org/data/2.5/"\
            "weather?q={}&units=metric&appid={}".format(location_name, api_key)
        r = requests.get(url)
        exception = False

    except requests.ConnectionError:
        print("Failed to establish a new connection: [Errno 11001]")
        exception = True

    if not exception:  # url response is not empty
        while(timer < 5):  # give five API calls to check the frequency
            url = "https: // api.openweathermap.org/data/2.5/weather?q = {}&" \
                "units = metric & appid = {}".format(location_name, api_key)

            r = requests.get(url)
            weather = r.json()

            city = str(weather['name'])
            code = str(weather['cod'])
            if code == "200":   # valid response from server
                print(api_frequency_count)
                # For a successful API call we should have the correct city
                assert city == location_name, \
                    "Unable to fetch data for {}".format(location_name)
            else:
                assert False, \
                        "Have you entred the spelling of city correctly?...#"

            api_frequency_count += 1
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))  # 1 sec sleep
            timer += 1

        api_frequency = api_frequency_count/5  # avereage API calls over 5 sec
        print("api_frequency = ", api_frequency, "Hz")
        assert api_frequency <= 1, \
            "API call frequency is {}, which is less than promised!" \
            .format(api_frequency)

    else:
        assert False, \
            "Failed to establish a new connection: [Errno 11001]"
