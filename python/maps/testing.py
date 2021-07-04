import json


def timeToString(seconds):
    minutes = int(0.5 + seconds/60)
    s = "{:0>2}"
    return (s + ":" + s).format(minutes // 60, minutes % 60)


print('\n    loading file')
with open("python/maps/shortestpaths.json") as file:
    data = json.load(file)


print('\n    getting first 5 only')

with open("python/maps/matrix.json") as file:
    matrix = json.load(file)

def pathUpdate(path):
    pairs = tuple(zip(path[:-1],path[1:]))
    output = [dict(start=s,stop=e,duration=matrix[s][e]["duration"],distance=matrix[s][e]["distance"]) for s,e in pairs]
    return output

newdict = {}

for k,v in data.items():
    newdict[k] = v[:5]

def toMiles(meters):
    d = meters / 1609.344
    if d < 100:
        d *= 10
        d += 0.5
        d = int(d)
        return d / 10
    else:
        return int(0.5 + d)


for each in newdict:
    for i in range(len(newdict[each])):
        newdict[each][i]["duration"] = timeToString(newdict[each][i]["duration"])
        newdict[each][i]["stdev"] = timeToString(newdict[each][i]["stdev"])
        newdict[each][i]["path"] = pathUpdate(newdict[each][i]["path"])
        for j in range(len(newdict[each][i]["path"])):
            newdict[each][i]["path"][j]["duration"] = timeToString(newdict[each][i]["path"][j]["duration"])
            newdict[each][i]["path"][j]["distance"] = toMiles(newdict[each][i]["path"][j]["distance"])

def printPath(path):
    width = {}
    for row in path:
        for k,v in row.items():
            w = len(str(v))
            if k not in width or width[k] < w:
                width[k] = w
    fin = "    "
    fin += "{duration:^" + str(width["duration"]) + "} "
    fin += "{start:<" + str(width["start"]) + "}"
    

    def splitDict(dicti):
        l,r = {}, {}
        for k,v in dicti.items():
            if k == "start":
                l[k] = v
                r[k] = ""
            else:
                l[k] = ""
                r[k] = v
        return l, r
        
    for row in path:
        first,second = splitDict(row)
        print(fin.format(**first))

        print(fin.format(**second))
        
    print(fin.format(start=path[-1]["stop"],duration="",distance=""))
    

print(json.dumps(newdict,indent=4,sort_keys=True))

for k in newdict:
    print(k)
    print()
    for i in range(len(newdict[k])):
        print(i+1)
        print()
        printPath(newdict[k][i]["path"])
        print()

