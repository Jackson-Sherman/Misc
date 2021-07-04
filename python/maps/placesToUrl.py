import json

with open('python/maps/places.json',) as file:
    places = json.load(file)

output = "https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyDIAv5PSciIzYg4B9edFs07hYGSXxiFd14&origins={0}&destinations={0}"

string = ""
for each in places:
    string += '|'
    string += each

string = string[1:]

print(output.format(string))