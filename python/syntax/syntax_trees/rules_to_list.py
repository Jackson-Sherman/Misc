import re

with open("/Users/jacksonsherman/Desktop/rules.txt", "r") as file:
    rules = file.read()

with open("/Users/jacksonsherman/Desktop/trees.txt", "r") as file:
    trees = file.read()

with open("/Users/jacksonsherman/Desktop/rules_syn.txt", "r") as file:
    rules_syn = file.read().lower()

with open("/Users/jacksonsherman/Desktop/rules_syn_regex.txt", "r") as file:
    rules_syn_regex = file.read().lower()

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
rules_syn = rules_syn.strip()
rules_syn_regex = rules_syn_regex.strip()
rules_syn = re.split("\n", rules_syn)
rules_syn_regex = re.split("\n", rules_syn_regex)
print(rules)

br()

#remove excess spaces and add brackets
rules = re.sub("\s*\n+\s*", "]\n[", rules)
rules = "[" + rules + "]"
print(rules)

br()

#replace arrows with single space and made lowercase
rules = re.sub("\s→\s", " ", rules)
rules = rules.lower()
print(rules)

br()

#turn rules into a list
list_of_rules = re.split("\n",rules)
print(list_of_rules)



br()
br()



print(trees)
trees = re.sub("\n", "", trees)
while re.search("\s\s+", trees):
    trees = re.sub("\s\s+", " ", trees)

br()

def printtree(t):
    st = t
    st = re.sub("\]\s+\]", "]]", st)
    st = re.sub("\]\s+\[", "][", st)

print(trees)

br()

search_string = "\[[^\]\s]+\s+([^\[\]]+\s*)+\]"
treecut = trees
outtree = ""

#gets rid of excess spaces
while re.search("\]\s+[\]\[]", trees):
    trees = re.sub("\]\s+\]", "]]", trees)
    trees = re.sub("\]\s+\[", "][", trees)

trees = trees.lower()

#turns trees from a string to a list of strings
string_of_trees = trees
trees = []
count = 0
curstring = ""
for i, char in enumerate(string_of_trees):
    if char == "[":
        count += 1
    curstring += char
    if char == "]":
        count -= 1
        if count == 0:
            trees += [curstring]
            curstring = ""        
print(trees)
br()

for i, this_tree in enumerate(trees):
    dom = [-1, -1]
    returntree = ""
    returntreedom = [-1, -1]
    for j, char in enumerate(this_tree):
        if char == "[":
            dom[0] = j
            returntreedom[0] = len(returntree)
            returntree += char
        elif char == "]":
            dom[1] = j + 1
            if 0 < dom[0]:
                currentlen = len(returntree)
                returntreedom[1] = len(returntree)
                dastring = this_tree[dom[0]:dom[1]]
                for x, rule in enumerate(list_of_rules):
                    if rule == dastring:
                        string = dastring
                        where = 0
                        while string[0] != " ":
                            returntree += string[0]
                            where = len(returntree)
                            string = string[1:]
                        returntree = returntree[:returntreedom[0]] + returntree[returntreedom[1]:]
                        
                returntree += "]"
            dom[0] = -1
            dom[1] = -1
        else:
            returntree += char
    trees[i] = re.sub("\s", "", returntree)

print(trees)

br()
for i, tree in enumerate(trees):
    distree = tree
    dif = True
    while tree != "[s]" and dif:
        for j, rule in enumerate(rules_syn):
            while rule in tree:
                tree.replace(rule, "[" + re.split("\[", rule)[1] + "]")
                print(tree)
        for j, rule in enumerate(rules_syn_regex):
            while re.search(rule, tree):
                match = re.search(rule, tree)
                span = match.span()
                string = match.string
                tree.replace(string, "[" + re.split("\[", string)[1] + "]")
        print(tree)
        dif = bool(tree != distree)
        distree = tree
        br()
    trees[i] = tree

br()

comment = """
asked V [NP _ {S/NP}]
wondered V [NP _ {S/PP}]
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