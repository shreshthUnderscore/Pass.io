import sqlite3

conn=sqlite3.connect('passdb.db')
c = conn.cursor()


c.execute("""CREATE TABLE Pass_DB (
    username text,
    userpass text,
    password text
)
""")

c.execute("SELECT *, oid FROM Pass_DB")
records=c.fetchall()
for i in records:
    print(i)