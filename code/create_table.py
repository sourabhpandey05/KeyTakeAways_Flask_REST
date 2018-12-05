import sqlite3

#initialize a connection

connection = sqlite3.connect("data.db") # file data.db is sqlite db

#cursor allows select things and start things like database, responsible to execute and store the queries and run the queries

cursor = connection.cursor()

create_table = "CREATE TABLE if NOT Exists users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)


create_table = "CREATE TABLE if NOT Exists items(name text,price real)"
cursor.execute(create_table)

create_table = "CREATE TABLE if NOT Exists BookList(id INTEGER PRIMARY KEY,title text,author text,publication text,tag text,userid INTEGER, FOREIGN KEY(userid) REFERENCES users(id))"
cursor.execute(create_table)

create_table = "CREATE TABLE if NOT Exists TakeAways(id INTEGER PRIMARY KEY,Keylearning text,userid INTEGER,bookid INTEGER,FOREIGN KEY(userid) REFERENCES users(id), FOREIGN KEY(bookid) REFERENCES BookList(id))"
cursor.execute(create_table)

connection.commit()

connection.close()