import sqlite3 as sql
import random
import math
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
c.execute("CREATE TABLE test(name TEXT, season INTEGER)")
rows = (
    ("Alice",1),
    ("Bob  ",1),
    ("Cindy",1),
    ("Dave ",1),
    ("Emma ",2),
    ("Fred ",2),
    ("Gail ",2),
    ("Helen",2),
    ("Alice",3),
    ("Cindy",3),
    ("Emma ",3),
    ("Helen",3),
    ("Ian  ",4),
    ("J'tia",4),
    ("Emma ",4),
    ("Mike ",5)
)
for row in rows:
    c.execute('INSERT INTO test VALUES("{0}",{1})'.format(*row))

connection.commit()

run("SELECT * FROM test")

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

c.execute("DROP TABLE IF EXISTS")

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