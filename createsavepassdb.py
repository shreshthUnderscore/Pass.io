import sqlite3

conn=sqlite3.connect('savepass.db')

c = conn.cursor()

c.execute("""CREATE TABLE save_pass (
    user text,
    pass text,
    oid_value text,
    domain text,
    username text,
    password text
)
""")

c.execute("SELECT *, oid FROM save_pass")
r=c.fetchall()
print(r)


