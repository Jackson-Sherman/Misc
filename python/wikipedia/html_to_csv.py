import re
from htmldom import htmldom
import random

with open("/Users/jacksonsherman/Desktop/Code/git/Personal/Misc/python/wikipedia/cropped_article.html") as file:
    string = file.read()
string = "<html>\n" + string + "\n</html>"

string = string.replace("&#93;",']')
string = string.replace("&#91;",'[')
string = string.replace("&#39;",'\'')
string = string.replace("&#160;",' ')
string = string.replace("&amp;",'&')

dom = htmldom.HtmlDom().createDom(string)

dom.find("*.reference").remove()
dom.find("span").remove()
dom.find("br").remove()
dom.find("small").remove()

# for i in dom.find("th, td").has("abbr, a"):
#     s = ''
#     for a in i.children(all_children=True):
#         s += i.

tables = dom.find("table.wikiepisodetable tbody")

temp = tables.html()
d = {}
l = {}
while '<' in temp:
    temp = temp[temp.index('<') + 1:]
    if '/' not in temp[:1]:
        s = ''
        while temp[0] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
            s += temp[0]
            temp = temp[1:]

        if s not in d:
            d[s] = 0

        d[s] += 1

        if temp[0] not in l:
            l[temp[0]] = 0

        l[temp[0]] += 1

    temp = temp[1:]

def dict_print(dictionary,sort_by_keys=True, asc=True):
    def unzip(t,v=[]):
        if len(t) == 0:
            return tuple(v)
        c = t[0]
        while len(v) < len(c):
            v += [()]
        for i in range(len(c)):
            v[i] += (c[i],)
        
    wk, wv = str(max([len(str(k)) for k in dictionary])), str(max([len(str(v)) for v in dictionary.values()]))

    valtodir = lambda va: '<' if isinstance(va,str) else '>'
    formed = lambda k,v: ('{k:'+valtodir(k)+wk+'}  {v:'+valtodir(v)+wv+'}').format(k=k,v=v)
    
    def sort_by_k(t):
        if len(t) < 2:
            return t

        pivot = t[random.randrange(0, len(t))]
        
        def split_it(ls, l=(), m=(), r=()):
            if not ls:
                return l, m, r
            
            tu,k = ls[:1], ls[0]

            if   k < pivot: l += tu
            elif pivot < k: r += tu
            else          : m += tu

            return split_it(ls[1:], l, m, r)
        
        l, m, r = split_it(t)
        return sort_by_k(l) + m + sort_by_k(r)
    
    def sort_by_v(it):
        if len(it) < 2:
            if it:
                return (it[0][0],)
            return ()
        _,pivot = it[random.randrange(0, len(it))]

        def split_it(ls, l=(), m=(), r=()):
            if not ls:
                return l, m, r
            
            p,(k,v) = ls[:1], (ls[0][:1], ls[0][1])

            if   v < pivot: l += p
            elif pivot < v: r += p
            else          : m += k

            return split_it(ls[1:], l, m, r)

        l, m, r = split_it(it)
        return sort_by_v(l) + m + sort_by_v(r)
    
    if sort_by_keys:
        order = sort_by_k(tuple(dictionary.keys()))[0::1 if asc else -1]
    else:
        order = sort_by_v(tuple(dictionary.items()))[::1 if asc else -1]
    
    for k in order:
        v = dictionary[k]
        print(formed(k,v))
    

dict_print(d,False)



# print(tables.first().html())

assert 1==2, "1!=2, bitch"

class html:
    def __init__(self, string):
        self.string = str(string)
        self.children = html._generate_children_list(self.string)
    
    def getElementById(self, id):
        pass

    def getElementsByTagName(self, tag):
        s, tag = self.string.upper(), str(tag).upper()

        indexes = []
    
    def getChildren(self):
        pass

    def _generate_children_list(string):
        pass

class textNode(html):
    def __init__(self, string=""):
        self.string = string
    
class element(html):
    def __init__(self, string):
        self.string = string
        self.tag = string
        def tagname(s, v=""):
            if not s:
                return v
            
            if re.match("[a-zA-Z]", s[0]):
                return tagname(s[1:], v + s[0])
            
            if re.match("[a-zA-Z][^a-zA-Z]", s[:2]):
                return v + s[0]
        def getAttributes(s):
            s = str(s)
            st = s[s.index(" ",s.index("<"))+1:s.find("/>") if 0 < s.find("/>") and s.find("/>") < s.index(">") else s.index(">")]
            ls = re.split("\s+",st)
            d = {}
            if 0 < len(ls):
                while 0 == len(ls[0]):
                    ls = ls[1:]
                while 0 == len(ls[-1]):
                    ls = ls[:-1]
                for each in ls:
                    l, r = each[:each.index("=")], each[each.index("=")+1:]
                    if 1 < len(r):
                        if r[0] in '\'\"':
                            r = r[1:]
                        if r[-1] in '\'\"':
                            r = r[:-1]
                    d[l] = r