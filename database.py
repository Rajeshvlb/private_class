import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXIST EMP(ID INT PRIMARY KEY, NAME TEXT, SALARY REAL)""")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(101, 'ABC', 80000)")
conn.execute("COMMIT")


c.execute("""SELECT * FROM EMP""")
print(next(c))

c.execute("UPDATE EMP SET SALATY = 60000 WHERE ID = 101")
conn.execute("COMMIT")

c.execute("""DELETE FROM EMP WHERE ID = 101""")
conn.execute("COMMIT")
