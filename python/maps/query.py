import json

def query(parks):
    def getPark(string):
        t = string[:2].lower()
        f = t[0]
        if f in 'ildgshcw' or t in ('ke','kn'):
            if t == 'ke':
                return "Kennywood"
            if t == 'kn':
                return "Knoebels"
            for park in parks:
                if park[0].lower() == f:
                    return park
        return None

    origin = getPark(input("    origin: "))
    while origin is None:
        print("error, try again")
        print(parks)
        origin = getPark(input("    origin: "))

    destination = getPark(input("    destination: "))
    while destination is None:
        print("error, try again")
        print(parks)
        destination = getPark(input("    destination: "))
    
    return origin, destination


def timeToString(seconds):
    minutes = int(0.5 + seconds/60)
    s = "{:0>2}"
    return (s + ":" + s).format(minutes // 60, minutes % 60)


if __name__ == "__main__":
    with open("python/maps/matrix.json","r") as file:
        matrix = json.load(file)
    
    parks = list(matrix.keys())
    parks.sort()
    while True:
        o, d = query(parks)
        print()
        print("    start: " + o)
        print("     stop: " + d)
        print("     time: " + timeToString(matrix[o][d]["duration"]))
        print("     dist: " + str(int(0.5 + matrix[o][d]["distance"] / 1609.344)))
        print()