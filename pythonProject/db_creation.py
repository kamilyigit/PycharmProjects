import sqlite3
from JIRA import jira_items

conn = sqlite3.connect('db_creation.db')

c = conn.cursor()

#c.execute("""CREATE TABLE fields (
#       issue_key text,
#       issue_type text,
#       created_time integer,
#       creator text,
#       status text,
#       summary text
#       )""")

#c.execute("INSERT INTO fields VALUES ('ARTBCRC - 2', 'Story' , '2022-07-16T18:55:40.000+0200', 'Joel' , 'Open', 'Test')")
#conn.commit()
print("debug")
c.execute("INSERT INTO fields VALUES (?,?,?,?,?,?)"),(jira_items)
conn.commit()


c.execute("SELECT*FROM fields WHERE issue_type='Story'")

print(c.fetchall())

conn.commit()

conn.close()