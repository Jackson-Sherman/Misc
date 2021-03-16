from c241 import Logic

def var_count(string):
    v = []
    c = string[::]
    while c[0] != ":":
        if c[0] in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            v.append(c[0])
        c = c[1:]
    return tuple(v)

def alter(string):
    string = str(string)
    pairs = (
        (",",";"),
        ("<>","="),("↔","="),
        ("\\(",""),("\\[",""),("\\]",""),("\\)",""),
        ("to",">"),("->",">"),("=>",">"),("\\to",">"),("→",">"),
        ("-","~"),("not","~"),("\\neg","~"),("¬","~"),
        ("*","&"),("and","&"),("\\wedge","&"),("∧","&"),
        ("%","^"),("xor","^"),("\\oplus","^"),("⊕","^"),
        ("+","|"),("v","|"),("or","|"),("\\vee","|"),("∨","|"),
        ("\\","")
    )
    for pair in pairs:
        while pair[0] in string:
            string = string.replace(*pair)
    string = string.replace("=","==")
    tups = tuple(string.split(";"))
    output = tuple()
    for each in tups:
        if each:
            output = output + (each,)
    return output

def ands(lst):
    if not lst:
        return True

    if lst[0]:
        return ands(lst[1:])

    return False

def varParse(funs):
    order = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    vars = tuple()
    for f in funs:
        este = set(f)
        for char in este:
            if char in order:
                vars = insertion(char,vars)
    return vars

def insertion(v,t):
    order = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    if len(t) < 1:
        return v,
    if order.index(v) == order.index(t[0]):
        return t
    elif order.index(v) < order.index(t[0]):
        return (v,) + t
    return t[:1] + insertion(v,t[1:])
    
def draw(lam,n,funs):
    t = (Logic(False),Logic(True))
    the_set = set()
    valid = set()
    vars = n
    n = len(vars)
    headers = vars + funs
    lens = tuple([len(h) for h in headers])
    first_line = "+"
    each_line_s = "|"
    for l in [*lens]:
        first_line += "-"*(l+2) + "+"
        each_line_s += " {:^" + str(l) + "} |"
    each_line = lambda v: each_line_s.format(*v)
    print(first_line)
    headers = list(headers)
    for i,h in enumerate(headers):
        h = h.replace("|","∨")
        h = h.replace("&","∧")
        h = h.replace("^","⊕")
        h = h.replace("~","¬")
        h = h.replace("=","↔")
        h = h.replace(">","→")
        headers[i] = h
    print(each_line(headers))
    def int2bintup(i,cuanto):
        s = bin(int(i))[2:]
        while len(s) < cuanto:
            s = "0" + s
        return tuple([Logic(char) for char in s])

    def validity(vals):
        return (not ands(vals[:-1])) or vals[-1]

    for i in range(2**n):
        cur = int2bintup(i,n)
        vals = list(cur) + [l(*cur) for l in lam]
        the_set |= {bool(vals[-1])}
        es_valid = bool(validity(vals[n:]))
        valid |= {es_valid}
        print(first_line)
        printme = each_line(vals)
        if not es_valid:
            printme = printme[:-1] + "+-invalid"
        print(printme)

    vals = {
        'Validity': len(lam)<2 or {True}==valid,
        'Satisfiable': {True}       <= the_set,
        'Contradiction': {False}    == the_set,
        'Tautology': {True}         == the_set,
        'Contingency': {True,False} == the_set
    }

    new_line = '+---------------+---+'

    if len(first_line) > len(new_line):
        first_line, new_line = new_line, first_line

    to_draw = ''
    for i in range(len(first_line)):
        if first_line[i] == "+" or new_line[i] == "+":
            to_draw += "+"
        else:
            to_draw += "-"
    to_draw += new_line[len(first_line):]
    print(to_draw)
    for k,v in vals.items():
        print('| {:>13} | {} |'.format(k,Logic(v)))
        print('+---------------+---+')

def loop():
    s = input("\n"+"*"*32+"\nProposition to evaluate:\n\n\t")
    print()

    if s:
        s = alter(s)
        v = varParse(s)
        va = ""
        for cada in v: va += "," + cada
        va = va[1:]
        functions = [eval("lambda " + va + ":" + string) for string in s]
        draw(functions,v,s)

        loop()



if __name__ == "__main__": loop()
