import json

with open("python/maps/matrix.json",) as file:
    data = json.load(file)

with open("python/maps/nicknames.json",) as file:
    nicknames = json.load(file)

def parse(inp, nick):

    def parse_aux(current):
        if isinstance(current, dict):
            return {parse_aux(k): parse_aux(v) for k, v in current.items()}
        if isinstance(current, (tuple,list)):
            return [parse_aux(v) for v in current]
        try:
            return nick[current]
        except KeyError:
            return current

    return parse_aux(inp)

json.dump(parse(data, nicknames), open("python/maps/matrix.json", 'w'), indent=4, sort_keys=True)