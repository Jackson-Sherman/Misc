import json
import numpy as np

class cycles:
    def __init__(self):
        self.cycles = set()

    def __contains__(self, value):
        for _ in range(len(value)):
            if value in self.cycles:
                return True
            value = cycles._rotate(value)
        return False
    
    def add(self, value):
        self.cycles |= set()

    def _form(value):
        index = value.index(min(value))
        return value[index:] + value[:index]

    def _rotate(value):
        return value[1:] + value[:1]
    
    def __ior__(self, other):
        pass

def shortestPath(graph, start="Home"):
    cities = list(graph.keys())
    cities.remove(start)
    cities.sort()
    permuted = permute(cities)

    addStart = lambda lista: (start,) + lista + (start,)
    def pathToCosts(path):
        output = {k: 0 for k in ("duration", "distance", "stdev")}
        pairs = tuple(zip((start,) + path, path + (start,)))
        for c, n in pairs:
            g = graph[c][n]
            output["duration"] += g["duration"]
            output["distance"] += g["distance"]

        output["stdev"] = np.std([graph[c][n]["duration"] for c, n in pairs])

        return output
    
    paths = []
    visited = set()
    for path in permuted:
        tp = tuple(path)
        if tp not in visited:
            visited |= {tp, tp[::-1]}
            val = dict(path=addStart(path), **pathToCosts(path))
            paths.append(val)

    return paths

def sortListBy(data, sortBy):
    data = tuple(data)
    
    def quicksort(values):
        if len(values) < 2:
            return values
        
        pivot = values[0]

        def sortAroundPivot(values):
            l, c, r = (), 0, ()

            s = pivot[sortBy]
            
            for v in values:
                if v[sortBy] < s:
                    l += (v,)
                elif s < v[sortBy]:
                    r += (v,)
                else:
                    c += 1
            
            return l, c, r

        l, c, r = sortAroundPivot(values[1:])
        return quicksort(l) + (pivot,) * (c+1) + quicksort(r)
    
    return quicksort(data)

def permute(data):
    def permute_aux(inp):
        if len(inp) < 2:
            return (inp,)
        output = ()
        for i in range(len(inp)):
            val, rest = inp[i:i+1], inp[:i] + inp[i+1:]
            for each in permute_aux(rest):
                output += (val + each,)
        
        return output
    
    return permute_aux(tuple(data))
    
print("\n    loading input\n")
with open("python/maps/matrix.json", "r") as file:
    matrix = json.loads(file.read())

print("\n    starting shortest path\n")
paths = shortestPath(matrix)
print("\n    creating output\n")
dur = sortListBy(paths, "duration")
dis = sortListBy(paths, "distance")
std = sortListBy(paths, "stdev")
output = {"duration": dur, "distance": dis, "stdev": std}

print("\n    saving output\n")
with open("python/maps/shortestpaths.json", "w") as file:
    json.dump(output, file, indent=4, sort_keys=True)
print("\n    done\n")