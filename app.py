# Displays arrival info for Toronto Pearson Airport (YYZ).

import http.client
import json
import pandas as pd

def torontoArivalsAirTest():

    conn = http.client.HTTPSConnection("toronto-pearson-airport.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "XXX",
        'X-RapidAPI-Host': "toronto-pearson-airport.p.rapidapi.com"
        }

    conn.request("GET", "/arrivals", headers=headers)

    res = conn.getresponse()
    data = res.read()

    flightData = (data.decode("utf-8"))
    jsonFD = json.loads(flightData)
    flightChart = pd.DataFrame(jsonFD)
#    print(type(jsonFD))
#    print(jsonFD)
#    print(jsonFD[1])
    print(flightChart)
    
        

torontoArivalsAirTest()
