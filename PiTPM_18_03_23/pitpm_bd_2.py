import sqlite3
from sqlite3 import Error
 
def sql_connection():
    try:
        con = sqlite3.connect('Town.db')
        return con
    except Error:
        print(Error)
 
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE Street(id integer PRIMARY KEY, name text)")
    con.commit()


def sql_insert(con, data):
    cursorObj = con.cursor()
    cursorObj.executemany("INSERT INTO Street VALUES(?, ?)", data)
    con.commit()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Street')
    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


con = sql_connection()
sql_fetch(con)
# sql_table(con)
data = [(1, "Улица1"), (2, "Улица2"), (3, "Улица5"), (4, "Улица4"), (5, "Улица5")]
# sql_insert(con, data)