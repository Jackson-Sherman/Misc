import re

tester_tree = """
[A
  [B]
  [C 
    [E 
      [V  hello]
      [W 
        [Y]
        [Z]
      ]
    ]
    [F]
  ]
  [D 
    [G]
    [H]
    [I 
      [K]
      [L 
        [M]
        [N 
          [R]
          [S 
            [T]
            [U]
          ]
        ]
        [O]
        [P]
        [Q]
      ]
    ]
    [J]
  ]
]
"""
tester_tree_good_str = \
{
    "A": {
        "B": {},
        "C": {
            "E": {
                "V": "hello",
                "W": {
                    "Y": {},
                    "Z": {}
                }
            },
            "F": {}
        },
        "D": {
            "G": {},
            "H": {},
            "I": {
                "K": {},
                "L": {
                    "M": {},
                    "N": {
                        "R": {},
                        "S": {
                            "T": {},
                            "U": {}
                        }
                    },
                    "O": {},
                    "P": {},
                    "Q": {}
                }
            },
            "J": {}
        }
    }
}

def bracket_to_dict(tree, debug_prints = False):

    def printem():
        print(tree)
        print("========")

    if debug_prints: printem()

    #remove line breaks
    tree = re.sub("\n", "", tree)
    if debug_prints: printem()

    #replace "[" and "]" with "{" and "}"
    tree = tree.replace("[", "{")
    tree = tree.replace("]", "}")
    if debug_prints: printem()

    #replacing duplicates
    

    #remove excess blank spaces
    tree = re.sub("\s+[{]", "{", tree)
    tree = re.sub("\s+[}]", "}", tree)
    tree = re.sub("\s+", " ", tree)
    tree = tree.strip()
    if debug_prints: printem()

    #adding quotes and colons
    while re.search("[{]\w+[}{\s]", tree):
        busca = re.search("[{]\w+[}{\s]", tree)
        match = busca.group()
        tree = tree.replace(match, "{\"" + match[1:-1] + "\": " + match[-1])

    while re.search("(\s\w+)+[}]", tree):
        busca = re.search("\s[\w\s]+[}]", tree)
        match = busca.group()
        tree = tree.replace(match, " \"" + match[2:-1] + "\"}")

    if debug_prints: printem()

    #moving brackets
    arbollist = re.split("[: ]", tree)
    treelist = []
    for x in arbollist:
        if x != "":
            treelist.append(x + ": ")

    tree = ""

    for i,j in enumerate(treelist):
        #if i < len(treelist):
        #    treelist[i] += ":"

        busca = re.search("[{]\"\w+\"[:]\s",treelist[i])

        if busca:
            match = busca.group()
            treelist[i] = treelist[i].replace(match, match[1:] + "{")
        
        tree += treelist[i]
        i+=1

    tree = tree[:-2]
    if debug_prints: printem()

    #adding commas between entries
    tree = re.sub("[}]", "}, ", tree)
    tree = re.sub("[}],\s$", "}", tree)
    while tree != re.sub("[}],\s?[}]", "}}", tree):
        tree = re.sub("[}],\s?[}]", "}}", tree)
    if debug_prints: printem()

    #remove extra brackets around lexical leaf nodes
    while re.search("[{]\"\w+\"[}]", tree):
        match = (re.search("[{]\"\w+\"[}]", tree)).group()
        tree = tree.replace(match, match[1:-1])
    if debug_prints: printem()

    #adding bracket around the whole thing
    tree = "{" + tree + "}"

    #replacing "{" with "{\n"
    tree = re.sub("[{]", "{\n", tree)
    tree = re.sub("[}]", "}\n", tree)
    tree = re.sub("[}]\n,\s", "},\n", tree)
    tree = re.sub(",\s", ",\n", tree)
    tree = re.sub("[{]\n[}]", "{}", tree)
    tree = re.sub("\n$", "", tree)
    if debug_prints: printem()

    #indenting
    old_tree = tree
    tree = ""
    bracket_count = 0
    for i,j in enumerate(old_tree):
        if j == "{":
            bracket_count += 1
        if j == "}":
            bracket_count -= 1
        string = ""
        issitu = -1 if j == "\n" and old_tree[i + 1] == "}" else 0
        string = " "*(bracket_count + issitu)*4 if j == "\n" else ""
        
        tree += j + string

    if debug_prints: printem()
    output = ""
    exec("output = " + tree)
    return output

def parentNode(child):
    pass

bracket_to_dict(tester_tree, True)

to = "→"
se = "\n"

def rules_to_list(string, char_converts, char_seperater):
    output = "out = [["
    strlist = re.split("[" + char_seperater + "]", string)
    #newlst = 
    for x in strlist:
        if x != "":
            string += x.strip()

    
    string = re.sub("w\+(\s\w+)*" + char_converts + "")
    for i,j in enumerate(input):
        pass
        #if j == 
