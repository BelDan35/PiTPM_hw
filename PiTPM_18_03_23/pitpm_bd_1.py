# # Создание соединения
# import sqlite3

# con = sqlite3.connect('mydatabase.db')

# # Курсор SQLite3

# con = sqlite3.connect('mydatabase.db')
# cursorObj = con.cursor()

# # Создание базы данных

# import sqlite3
 
# from sqlite3 import Error
 
# def sql_connection():
#     try:
#         con = sqlite3.connect(':memory:')
#         print("Connection is established: Database is created in memory")
#     except Error:
#         print(Error)
#     finally:
#         con.close()

# sql_connection()

# # Создание таблицы

# import sqlite3
 
# from sqlite3 import Error
 
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)

# def sql_table(con):
#     cursorObj = con.cursor()
#     cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
#     con.commit()
 
# con = sql_connection()
# sql_table(con)

# # Вставка данных в таблицу

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_insert(con, entities):
#     cursorObj = con.cursor()
#     cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
#     con.commit()
 
# entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
# sql_insert(con, entities)

# # Обновление таблицы

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_update(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
#     con.commit()
 
# sql_update(con)

# # Оператор SELECT

# cursorObj.execute('SELECT * FROM employees ')
# cursorObj.execute('select column1, column2 from tables_name FROM employees')

# # Выборка всех данных

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_fetch(con):
 
#     cursorObj = con.cursor()
#     # cursorObj.execute('SELECT * FROM employees')
#     # cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
#     rows = cursorObj.fetchall()

#     for row in rows:
#         print(row)
 
# sql_fetch(con)

# # SQLite3 rowcount

# print(cursorObj.execute('SELECT * FROM employees').rowcount)
# rows = cursorObj.fetchall()
# print(len(rows))
# print(cursorObj.execute('DELETE FROM employees').rowcount)

# # Список таблиц

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('SELECT name from sqlite_master where type= "table"')
#     print(cursorObj.fetchall())
 
# sql_fetch(con)

# # Проверка существования таблицы

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('create table if not exists projects(id integer, name text)')
#     cursorObj.execute('drop table if exists projects')
#     cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')
#     con.commit()
# print(cursorObj.fetchall())
# sql_fetch(con)

# # Удаление таблицы

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
 
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('DROP table if exists employees')
#     con.commit()
 
# sql_fetch(con)

# # Исключения SQLite3

# # Массовая вставка строк в Sqlite

# import sqlite3
 
# con = sqlite3.connect('mydatabase.db')
# cursorObj = con.cursor()
# cursorObj.execute('create table if not exists projects(id integer, name text)')
# data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
# cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
# con.commit()

# # Закрытие соединения

# con = sqlite3.connect('mydatabase.db')
# con.close()

# # SQLite3 datetime

import sqlite3
import datetime
 
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
con.commit()

