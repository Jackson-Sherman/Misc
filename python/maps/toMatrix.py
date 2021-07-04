import json

with open("python/maps/original.json") as file:
    original = json.loads(file.read())

output = {}

if original["status"] == "OK":
    origins = original["origin_addresses"]
    destinations = original["destination_addresses"]
    cities = list(set(origins) | set(destinations))
    cities.sort()
    for i in range(len(origins)):
        for j in range(len(destinations)):
            element = original["rows"][i]["elements"][j]
            if element["status"] == "OK":
                value = {key: element[key]["value"] for key in ("distance", "duration")}
                if origins[i] not in output:
                    output[origins[i]] = {}
                output[origins[i]][destinations[j]] = value
    
    string = json.dumps(output, sort_keys=True, indent=4)
    with open("python/maps/matrix.json", "w") as file:
        file.write(string)