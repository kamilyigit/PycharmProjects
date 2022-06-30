import sqlite3
from JIRA import jira_items

conn = sqlite3.connect('db_creation.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE fields (
           issue_key text,
           issue_type text,
           created_time integer,
           creator text,
           status text,
           summary text)
           """)
    print("table is created!")
    conn.close()
def drop_table():
    c.execute("DROP TABLE fields")
    print("table is dropped")
    conn.commit()
def example_entry():
    c.execute("INSERT INTO fields VALUES ('ARTBCRC - 2', 'Story' , '2022-07-16T18:55:40.000+0200', 'Joel' , 'Open', 'Test')")
    conn.commit()
print("debug")

list_key=list(jira_items["Key"])
list_type=list(jira_items["Type"])
list_created_time=list(jira_items["Created_Time"])
list_creator=list(jira_items["Creator"])
list_status=list(jira_items["Status"])
list_summary=list(jira_items["Summary"])

def add_item():
    for i in range(len(list_key)):
        c.execute("""INSERT INTO fields ( issue_key, issue_type, created_time, creator, status, summary) VALUES (?,?,?,?,?,?)""",
                  (list_key[i],list_type[i],list_created_time[i],list_creator[i],list_status[i],list_summary[i]))
        conn.commit()
    print("Data is inserted!")
def refresh_table():
    c.execute("""DELETE FROM fields;""")
    conn.commit()
    print("Table refreshed!")

add_item()

#print(f"Added data {i['fpath']}")  # print a helpful message once added
c.execute("SELECT*FROM fields WHERE issue_key='ARTBCRC-33475'")

print(c.fetchone())
conn.close()

