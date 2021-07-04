import urllib.request
import json
import numpy as np
import random
from PIL import Image

# text = urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins=8211+Castlebrook+Dr+46256&destinations=46040&key=AIzaSyDIAv5PSciIzYg4B9edFs07hYGSXxiFd14").read()
# data = json.loads(text)
# print(json.dumps(data,indent=4))

def urlget(latitude, longitude):
    return "https://maps.googleapis.com/maps/api/distancematrix/json?origins=8211+Castlebrook+Dr+46256&key=AIzaSyDIAv5PSciIzYg4B9edFs07hYGSXxiFd14&destinations=" + str(latitude) + '+' + str(longitude)

data = json.loads("""{
    "destination_addresses": [
        "Fishers, IN 46040, USA"
    ],
    "origin_addresses": [
        "8211 Castlebrook Dr, Indianapolis, IN 46256, USA"
    ],
    "rows": [
        {
            "elements": [
                {
                    "distance": {
                        "text": "17.3 km",
                        "value": 17333
                    },
                    "duration": {
                        "text": "20 mins",
                        "value": 1173
                    },
                    "status": "OK"
                }
            ]
        }
    ],
    "status": "OK"
}""")

def status(result):
    return result["rows"][0]["elements"][0]["status"] == "OK"

def state(result):
    text = result["destination_addresses"][0]
    splitit = text.split(', ')
    if splitit[-1] == 'USA':
        return splitit[-2][:2]
    else:
        return None

def time(result):
    return result["rows"][0]["elements"][0]["duration"]["value"]

minpx = 100
p0 = 41.105204, -74.094934
p1 = 40.495525, -73.511170
dif = p1[0] - p0[0], p1[1] - p0[1]
s = min(dif) / minpx
lon = tuple(np.arange(min(p0[0],p1[0]),max(p0[0],p1[0])+s/2,s))
lat = tuple(np.arange(min(p0[1],p1[1]),max(p0[1],p1[1])+s/2,s))[::-1]
output = np.zeros((len(lat),len(lon)))
statecolor = {}
y = 0
for la in lat:
    x = 0
    for lo in lon:
        url = urlget(la,lo)
        data = json.loads(urllib.request.urlopen(url).read())
        este = state(data)
        if este not in statecolor:
            calc = lambda: int(0x100 * random.random())
            statecolor[este] = calc, calc, calc
        output[y][x] = statecolor[este]
        x+=1
    y+=1

img = Image.fromarray(output)
img.save("okthen.png")
img.show()
# long = tuple(range(-125,-65.99999,step))
# lat = tuple(range(25,49.000001,step))