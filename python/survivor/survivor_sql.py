import sqlite3 as sql
import random

connection = sql.connect("python/survivor/survivor.db")
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS test")
c.execute("CREATE TABLE test(name TEXT, season TEXT)")
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
    c.execute('INSERT INTO test VALUES("{0}","{1}")'.format(*row))

connection.commit()

def run(string):
    for i in c.execute(string):
        if 1 < len(i):
            s = ""
            for each in i:
                s += str(each) + " "
            print(s[:-1])
        else:
            print(i[0])
    print("\n" + "*"*20 + "\n")

run("SELECT * FROM test")

run("""SELECT season FROM test WHERE name = '{0}'""".format(*rows[0]))

run("""
SELECT SUBSTR('...',1,3*(name <> '{0}')) || name, season FROM test WHERE 
(
    name = '{0}'
    AND
    season = {1}
) OR ((
        season IN (
            SELECT season FROM test WHERE name = '{0}'
        )
    )
)
""".format(*rows[0]))

# run("""
# WITH RECURSIVE
#     under(name, season) AS (
#         VALUES({0},{1})
#     )
# """.format(*rows[0]))

class Randset:
    def __init__(self, iterable):
        self.set = []
        self.len = 0
        for i in iterable:
            self.set.append(i)
            self.len += 1

    def getlength(self):
        return self.len
    
    def empty(self):
        return not bool(self.set)

    def push(self, *vals):
        for each in vals:
            self.set += [each]
            self.len += 1
    
    def pop(self):
        i = int(random.random() * self.len)
        p = self.set[i]
        self.set = self.set[:i] + self.set[i+1:]
        self.len -= 1
        return p
    
    def randomize(self):
        output = []
        while not self.empty():
            output.append(self.pop())
        return output
    

c.execute('DROP TABLE IF EXISTS edge')
c.execute('CREATE TABLE edge(aa INT, bb INT)')
c.execute('CREATE INDEX edge_aa ON edge(aa)')
c.execute('CREATE INDEX edge_bb ON edge(bb)')
conns = (
    (1,3),
    (2,3),
    (2,4),
    (2,5),
    (3,5),
    (4,5)
)
conns = Randset([Randset(i) for i in conns])
while not conns.empty():
    internal = conns.pop()
    c.execute('INSERT INTO edge VALUES({0},{1})'.format(internal.pop(),internal.pop()))
# c.execute('INSERT INTO edge VALUES(11,-1)')
# c.execute('INSERT INTO edge VALUES(12,-1)')
# c.execute('INSERT INTO edge VALUES(13,-1)')
# c.execute('INSERT INTO edge VALUES(14,-1)')
# c.execute('INSERT INTO edge VALUES(21,-2)')
# c.execute('INSERT INTO edge VALUES(22,-2)')
# c.execute('INSERT INTO edge VALUES(23,-2)')
# c.execute('INSERT INTO edge VALUES(24,-2)')
# c.execute('INSERT INTO edge VALUES(31,-3)')
# c.execute('INSERT INTO edge VALUES(32,-3)')
# c.execute('INSERT INTO edge VALUES(33,-3)')
# c.execute('INSERT INTO edge VALUES(34,-3)')
# c.execute('INSERT INTO edge VALUES(41,-4)')
# c.execute('INSERT INTO edge VALUES(42,-4)')
# c.execute('INSERT INTO edge VALUES(43,-4)')
# c.execute('INSERT INTO edge VALUES(51,-5)')
connection.commit()

run("""SELECT * FROM edge""")

run("""
WITH RECURSIVE
    nodes(x) AS (
        SELECT 2
        UNION
        SELECT aa FROM edge JOIN nodes ON bb=x
    )
SELECT x FROM nodes;
""".format(*rows[0]))

connection.close()