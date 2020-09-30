import re

with open("/Users/jacksonsherman/Desktop/rules.txt", "r") as file:
    rules = file.read()

with open("/Users/jacksonsherman/Desktop/trees.txt", "r") as file:
    trees = file.read()

def br():
    print("\n~    ~~   ~~~  ~~~~ ~~~~~ ~~~~  ~~~   ~~    ~\n")

def within(index, iterable):
    if index <= 0:
        return 0
    elif len(iterable) - 1 < index:
        return len(iterable) - 1
    else:
        return index

rules = rules.strip()
print(rules)

br()

#remove excess spaces and add brackets
rules = re.sub("\s*\n+\s*", "]\n[", rules)
rules = "[" + rules + "]"
print(rules)

br()

#replace arrows with single space
rules = re.sub("\s→\s", " ", rules)
print(rules)

br()

#turn rules into a list
list_of_rules = re.split("\n",rules)
print(list_of_rules)



br()
br()



print(trees)   #"[" + not("]")*{1,} 
trees = re.sub("\n", "", trees)
while re.search("\s\s+", trees):
    trees = re.sub("\s\s+", " ", trees)

br()

def printtree(t):
    st = t
    st = re.sub("\]\s+\]", "]]", st)
    st = re.sub("\]\s+\[", "][", st)

print(trees)
thid = True

br()

search_string = "\[[^\]\s]+\s+([^\[\]]+\s*)+\]"
treecut = trees
outtree = ""

#gets rid of excess spaces
while re.search("\]\s+[\]\[]", trees):
    trees = re.sub("\]\s+\]", "]]", trees)
    trees = re.sub("\]\s+\[", "][", trees)

print(trees)

comment = """
while re.search(search_string, trees) and thid:
    domain = re.search(search_string, trees).span()
    string = re.search(search_string, trees).string
    print(string)
    tree_start_end = (trees[:domain[0]], trees[domain[1]:])
    outstring = ""
    space_not_found = True
    while string:
        char = string[0]
        if char == " " and space_not_found:
            space_not_found = False
            outstring += "→"
        else:
            outstring += char

        string = string[1:]
    outstring += string
    print(outstring + "\n")
    thid = False
    trees = tree_start_end[0] + outstring + tree_start_end[1]



arbol = ""
while re.search()
for i, char in enumerate(trees):
    if char == "\n":
        pass
    
    elif re.search("[^\[\]]\s[^\[\]]", trees[i - 1:i + 2]):
        arbol += char

    elif char == " ":
        pass
"""