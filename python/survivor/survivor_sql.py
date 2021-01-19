import sqlite3 as sql
import random
import math
import sys
sys.path.append('/Users/jacksonsherman/VSC/Misc')
from python.modules.abstract_data import Queue, Stack
connection = sql.connect("python/survivor/survivor.db")
c = connection.cursor()

def execute(string):
    strings = string.split(";")
    for each in strings:
        each = each.strip()
        if each:
            c.execute(each)

def run(strings,*formatargs):
    inn = strings.split(";")
    out = ""
    l = 0
    for string in inn:
        string = string.strip()
        if string:
            if formatargs:
                string = string.format(*formatargs)
            for i in c.execute(string):
                curl = 0
                out += "\n"
                if 1 < len(i):
                    s = ""
                    for each in i:
                        s += str(each) + " "
                    out += s[:-1]
                    curl = len(s[:-1])
                else:
                    out += str(i[0])
                    curl = len(str(i[0]))
                
                if curl > l:
                    l = curl
    b = 2
    l = l+b
    l = min(l,60)
    print("{o}\n{i}{}\n{i}\n{o}\n".format(out,o="*"*l,i=" "*(l-1)+"*"))

def mandel(a=' ░▒▓█',iteration_max=32):
    if isinstance(a, str):
        if len(a) == 5:
            a = tuple([a[i] for i in range(5)])
        elif ";" in a:
            a = a.split(";")
        elif "," in a:
            a = a.split(",")
    a = list(a)
    for i in range(len(a)):
        if len(a[i]) == 1:
            a[i] = "'" + a[i] + "'"
    a = tuple(a)
    run('''
    WITH RECURSIVE
      xaxis(x) AS (VALUES(-min(2.0,2.0)) UNION ALL SELECT x+0.05 FROM xaxis WHERE x<0.471185334933396),
      yaxis(y) AS (VALUES(-min(1.1,1.122757063632597)) UNION ALL SELECT y+0.1  FROM yaxis WHERE y<1.122757063632597),
      m(iter, cx, cy, x, y) AS (
        SELECT 0, x, y, 0.0, 0.0 FROM xaxis, yaxis
        UNION ALL
        SELECT iter+1, cx, cy, x*x-y*y + cx, 2.0*x*y + cy FROM m 
        WHERE (x*x + y*y) < 4.0 AND iter<{iter}
      ),
      m2(iter, cx, cy) AS (
        SELECT max(iter), cx, cy FROM m GROUP BY cx, cy
      ),
      a(r,t) AS (
        SELECT random(),
        group_concat(
          CASE 
            WHEN iter<{iter}*0.26303441 THEN {}
            WHEN iter<{iter}*0.48542683 THEN {}
            WHEN iter<{iter}*0.67807191 THEN {}
            WHEN iter<{iter}*0.84799691 THEN {}
            ELSE {}
          END, 
          ''
        )
        FROM m2 GROUP BY cy
      )
    SELECT group_concat(rtrim(t),x'0a') FROM a
    '''.format(*a,iter=iteration_max))
mandel()
mandel((" ",
"CASE WHEN random() < 0xc000000000000000 THEN '▖' WHEN random() < 0xd555555555555555 THEN '▗' WHEN random() < 0x0000000000000000 THEN '▘' ELSE '▝' END",
"CASE WHEN random() < 0xaaaaaaaaaaaaaaaa THEN '▀' WHEN random() < 0xb333333333333333 THEN '▄' WHEN random() < 0xc000000000000000 THEN '▌' WHEN random() < 0xd555555555555555 THEN '▐' WHEN random() < 0x0000000000000000 THEN '▚' ELSE '▞' END",
"CASE WHEN random() < 0xc000000000000000 THEN '▙' WHEN random() < 0xd555555555555555 THEN '▛' WHEN random() < 0x0000000000000000 THEN '▜' ELSE '▟' END",
"█"
))
mandel(' .+*#')
c.execute("DROP TABLE IF EXISTS test")
heads = ('name', 'season')
c.execute("CREATE TABLE test({0} TEXT, {1} INTEGER)".format(*heads))
rows = (
    ("Alice",1),
    ("Bob--",1),
    ("Cindy",1),
    ("Dave-",1),
    ("Emma-",2),
    ("Fred-",2),
    ("Gail-",2),
    ("Helen",2),
    ("Alice",3),
    ("Cindy",3),
    ("Emma-",3),
    ("Helen",3),
    ("Ian--",4),
    ("J'tia",4),
    ("Emma-",4),
    ("Mike-",5)
)
for row in rows:
    c.execute('INSERT INTO test VALUES("{0}",{1})'.format(*row))

connection.commit()

run("SELECT name, season FROM test ORDER BY season, name")

run("""SELECT season FROM test WHERE name = '{0}'""".format(*rows[0]))

run("""
SELECT 
CASE name 
    WHEN '{0}'
    THEN substr(
        CASE rowid
            WHEN (SELECT min(rowid) FROM test WHERE name = '{0}')
            THEN 'k' || name || x'0a'
            ELSE 'k'
        END || ' | ' || substr('0' || CAST(season AS TEXT),2*(9 < season)),2)
    ELSE ' | | ' || name
END
FROM test 
WHERE season IN (SELECT season FROM test WHERE name = '{0}')
""", *rows[0])

run('''
WITH RECURSIVE
    pairs(n1, n2, s) AS (
        SELECT name, NULL, season FROM test
        UNION ALL
        SELECT n1, name, s 
            FROM pairs JOIN test ON s = season AND n1 <> name
    )
SELECT * FROM pairs WHERE n2 ORDER BY s, n1, n2
'''[:0])

execute("""
DROP TABLE IF EXISTS edges;
CREATE TABLE edges (name1 TEXT, name2 TEXT, season INTEGER);
WITH initial(n,s) AS (SELECT name, season FROM test)
INSERT INTO edges SELECT n, name, s FROM initial JOIN test ON n <> name AND s = season WHERE (name, n, s) NOT IN edges ORDER BY s, n, name
""")
connection.commit()

run('SELECT * FROM edges')

run('''
WITH RECURSIVE nodes(x) AS (
   SELECT 'Alice'
   UNION
   SELECT name2 FROM edges JOIN nodes ON name1=x
)
SELECT x FROM nodes;
''')

def sortby(lista,dic):
    dic = dict(dic)
    lista = list(lista)
    for i in range(len(lista) - 1):
        for j in range(i+1,len(lista)):
            if dic[lista[i]] > dic[lista[j]]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

class Pytable:
    def __init__(self, *headers):
        '''
        Creates table with the column names given
        '''
        self.headers = tuple([each for each in headers])
        self.data = []
    
    def insert_one(self, row, *args):
        if args:
            vals = tuple([row] + [each for each in args])
        else:
            try:
                vals = tuple(row)
            except:
                vals = tuple(row,)

        self.data.append(vals)

    def insert_many(self, rows, *args):
        if args:
            self.insert_one(rows)
            for each in args:
                self.insert_one(each)
        else:
            for each in rows:
                self.insert_one(each)

def toPy(headers,entries):
    output = []
    for row in entries:
        d = dict()
        for h,r in zip(headers,row):
            d[h] = r#.strip() if isinstance(r, str) else r
        output.append(d)
    return output

x = toPy(heads,rows)

for each in x:
    print(each)

def index(lista, entry):
    for i in range(len(lista)):
        if lista[i][0] == entry:
            return i
    return -1

def dijkstra(graph, source):
    Q = [] # vertex set

    parent = {}
    depth = {}
    original_order = {}
    for each in graph:
        parent[each] = None
        depth[each] = float('inf')
        if original_order:
            prev = original_order.popitem()
            original_order[prev[0]] = prev[1]
            original_order[each] = prev[1] + 1
        else:
            original_order[each] = 0
        Q.append(each)
    depth[source] = 0
    while Q: # is not empty
        u = Q[0] # u is the vertex in Q with the minimum depth from the source
        for v in Q:
            if depth[v] < depth[u]:
                u = v
        Q.remove(u)

        try:
            similarity = lambda tup: None if len(u) != len(tup) else sum([1 if u[i] == tup[i] else 0 for i in range(len(u))])/len(u)
        except:
            similarity = lambda val: 1 if u == val else 0

        for v in Q:
            if 0 < similarity(v):
                alt = depth[u] + 1
                if alt < depth[v]:
                    depth[v] = alt
                    parent[v] = u
    
    def childs(g, v={}):
        if g:
            daughter, mother = g.popitem()
            if mother not in v:
                v[mother] = set()
            v[mother].add(daughter)
            return childs(g,v)
        else:
            return v

    children = childs(parent.copy())

    return depth, parent, children, original_order

d,p,c,order = dijkstra(rows,rows[0])
print()
children = c.copy()
for mom in children:
    samename, differentname = [], []
    while children[mom]:
        daughter = children[mom].pop()
        try:
            b = bool(daughter[0] == mom[0])
        except:
            try:
                b = bool(daughter[0] == mom)
            except:
                try:
                    b = bool(daughter == mom[0])
                except:
                    b = bool(daughter == mom)
        if b:
            i = 0
            if samename:
                cont = True
                while i<len(samename) and cont:
                    if order[daughter] < order[samename[i]]:
                        cont = False
                        samename = samename[:i] + [daughter] + samename[i:]
                    i += 1
                if cont:
                    samename.append(daughter)
            else:
                samename = [daughter]
        else:
            i = 0
            if differentname:
                cont = True
                while i<len(differentname) and cont:
                    if order[daughter] < order[differentname[i]]:
                        cont = False
                        differentname = differentname[:i] + [daughter] + differentname[i:]
                    i += 1
                if cont:
                    differentname.append(daughter)
            else:
                differentname = [daughter]
    children[mom] = samename + differentname
for each in children:
    print(str(each)+': '+str(children[each]))

for row in rows:
    if row in children:
        dad,sons = row,children[row]
        first = True
        for son in sons:
            if first:
                first = False
                print('\n    {:12}: {}'.format(str(dad),str(son)))
            else:
                print('    |'+' '*13+str(son))

print()

def present(hijos):
    s = Stack()
    def tostr(row):
        if isinstance(row,None):
            return None
        elif len(row) > 1:
            return str(row[0]) + tostr(row[1:])
        elif row:
            return str(row[0])
        else:
            return ''
    s.push((rows[0],0))
    output = []
    visited = set()
    while not s.empty():
        current, level = s.pop()
        output.append((current,level))
        visited |= {current}
        print('tostr(current))

present(children)

print()
for entry in rows:
    ri = order[entry]
    pa = p[entry]
    de = d[entry]
    print(('{:>2}{:^14}comes from{:^14}after{:^5}steps').format(str(ri),str(entry),str(pa),str(de)))
print()



def connections(todo,name):
    unvisited = todo
    visited = []
    q = Stack()
    for char in name:
        if char != '-':
            print(char, end='')
    print()
    for each in todo[::-1]:
        if each['name'] == name:
            q.push((each,1))
    while not q.empty():
        # print("\n" + "="*9 + "\n")
        # print("q: {0}\nv: {1}\nu: {2}".format(q, visited, unvisited))
        now = q.pop()
        current = now[0]
        level = now[1]
        s = " | "*level
        if level % 2 == 1:
            s = s[:-2]
            s += "+----" + str(current['season'])
        else:
            s = s[:-2]
            s += '+-' + current['name'] + '-' + str(current['season'])
        print(s)
        if current in unvisited:
            visited.append(now)
            unvisited.remove(current)
            if level % 2 == 1:
                hijos = [row for row in todo if row['season'] == current['season']]
                for kid in hijos:
                    if kid != current and kid in unvisited:
                        q.push((kid, level + 1))
            else:
                hijos = [row for row in todo if row['name'] == current['name']]
                for kid in hijos:
                    ind = index(visited,kid)
                    if kid != current and kid in unvisited:
                        q.push((kid, level + 1))
                    elif -1 < ind and kid not in unvisited and level + 1 < visited[ind][1]:
                        visited = visited[:ind] + visited[ind+1:]
        
    return visited
v = x[0]
connections(x,v['name'])

# total = []
# di = {}
# k = 0
# for a in (0,1,2):
#     for b in (0,1,2):
#         for c in (0,1,2):
#             for d in (0,1,2):
#                 for e in (0,1,2):
#                     for f in (0,1,2):
#                         for g in (0,1,2):
#                             for h in (0,1,2):
#                                 for i in (0,1,2):
#                                     print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i))
#                                     k += 1
#                                     also = [0,0,0]
#                                     also[a] += 1
#                                     also[b] += 1
#                                     also[c] += 1
#                                     also[d] += 1
#                                     also[e] += 1
#                                     also[f] += 1
#                                     also[g] += 1
#                                     also[h] += 1
#                                     also[i] += 1
#                                     if also[0] < also[1]:
#                                         also[0], also[1] = also[1], also[0]
#                                     if also[1] < also[2]:
#                                         also[1], also[2] = also[2], also[1]
#                                     if also[0] < also[1]:
#                                         also[0], also[1] = also[1], also[0]
#                                     also = tuple(also)
#                                     total += [also]
#                                     if also not in di:
#                                         di[also] = 0
#                                     di[also] += 1

# for k,v in di.items():
#     print('{}-{}-{}: {:>4}: {:%}'.format(*k, v, v/len(total)))

# m = list(di.items())
# for i in range(len(m)-1):
#     for j in range(i+1, len(m)):
#         if m[i][1] > m[j][1]:
#             m[i], m[j] = m[j], m[i]
# print('\n===================\n')
# for k,v in m:
#     print('{}-{}-{}: {:>4}: {:%}'.format(*k, v, v/len(total)))

# run("SELECT * FROM ")

# run('''
# WITH RECURSIVE
#     sub(outp, n, s, followup, level) AS (
#         SELECT 'Alice', 'Alice', 1, 1, 0
#         UNION
#         SELECT 
#             CASE name 
#                 WHEN n
#                 THEN ' | ' || substr('0' || CAST(season AS TEXT),2*(9 < season))
#                 ELSE ' | | ' || name
#             END,
#             name,
#             season,
#             (name <> n),
#             level + 1
#         FROM test JOIN sub ON followup
#         WHERE season IN (SELECT season FROM test WHERE name = n)
#     )
# SELECT outp FROM sub
# ''')


# run("""
# SELECT '{1}';
# WITH RECURSIVE
#     initial(name, season, level) AS (
#         SELECT name, season, 1 FROM test WHERE test.name = '{1}'
#         UNION
#         SELECT test.name, test.season, initial.level + 1
#     ),
#     samename(name, season, level) AS (
#         SELECT name, 0, 0 FROM test WHERE rowid = 1
#         UNION
#         SELECT test.name, test.season, samename.level + 1
#             FROM samename JOIN test ON samename.name = test.name
#         ORDER BY 3
#     )

# SELECT SUBSTR('{0}',1,level*3) || name, season FROM initial WHERE level > 0 LIMIT 15
# """.format(' | '*20,*rows[0]))

# class Randset:
#     def __init__(self, iterable):
#         self.set = []
#         self.len = 0
#         for i in iterable:
#             self.set.append(i)
#             self.len += 1

#     def getlength(self):
#         return self.len
    
#     def empty(self):
#         return not bool(self.set)

#     def push(self, *vals):
#         for each in vals:
#             self.set += [each]
#             self.len += 1
    
#     def pop(self):
#         i = int(random.random() * self.len)
#         p = self.set[i]
#         self.set = self.set[:i] + self.set[i+1:]
#         self.len -= 1
#         return p
    
#     def randomize(self):
#         output = []
#         while not self.empty():
#             output.append(self.pop())
#         return output
    

# c.execute('DROP TABLE IF EXISTS edge')
# c.execute('CREATE TABLE edge(aa INT, bb INT)')
# c.execute('CREATE INDEX edge_aa ON edge(aa)')
# c.execute('CREATE INDEX edge_bb ON edge(bb)')
# conns = (
#     (1,3),
#     (2,3),
#     (2,4),
#     (2,5),
#     (3,5),
#     (4,5)
# )
# conns = Randset([Randset(i) for i in conns])
# while not conns.empty():
#     internal = conns.pop()
#     c.execute('INSERT INTO edge VALUES({0},{1})'.format(internal.pop(),internal.pop()))
# # c.execute('INSERT INTO edge VALUES(11,-1)')
# # c.execute('INSERT INTO edge VALUES(12,-1)')
# # c.execute('INSERT INTO edge VALUES(13,-1)')
# # c.execute('INSERT INTO edge VALUES(14,-1)')
# # c.execute('INSERT INTO edge VALUES(21,-2)')
# # c.execute('INSERT INTO edge VALUES(22,-2)')
# # c.execute('INSERT INTO edge VALUES(23,-2)')
# # c.execute('INSERT INTO edge VALUES(24,-2)')
# # c.execute('INSERT INTO edge VALUES(31,-3)')
# # c.execute('INSERT INTO edge VALUES(32,-3)')
# # c.execute('INSERT INTO edge VALUES(33,-3)')
# # c.execute('INSERT INTO edge VALUES(34,-3)')
# # c.execute('INSERT INTO edge VALUES(41,-4)')
# # c.execute('INSERT INTO edge VALUES(42,-4)')
# # c.execute('INSERT INTO edge VALUES(43,-4)')
# # c.execute('INSERT INTO edge VALUES(51,-5)')
# connection.commit()

# run("""SELECT * FROM edge""")

# run("""
# WITH RECURSIVE
#     nodes(x) AS (
#         SELECT 2
#         UNION
#         SELECT aa FROM edge JOIN nodes ON bb=x
#     )
# SELECT x FROM nodes;
# """.format(*rows[0]))

connection.close()