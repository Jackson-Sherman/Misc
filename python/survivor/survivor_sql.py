import sqlite3 as sql

connection = sql.connect("python/survivor/survivor.db")
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS test")
c.execute("CREATE TABLE test (name TEXT, season INTEGER)")
c.execute("INSERT INTO test VALUES('ok',1),('no',1)")

connection.commit()

for i in c.execute("SELECT * FROM test"):
    print(i)

connection.close()