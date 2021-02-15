import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="SQLpassWord789",
    auth_plugin='mysql_native_password',
    database="pwords",
    )

# checking if connection is successful
# print(db_connection)

my_cursor = db_connection.cursor()
# my_cursor.execute("CREATE DATABASE testdb")

# check if database has been created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

# my_cursor.execute("CREATE DATABASE pwords")

# my_cursor.execute("CREATE TABLE passwords (website VARCHAR(255), username VARCHAR(255), pword VARCHAR(255))")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])

insertion = "INSERT INTO passwords (website, username, pword) VALUES (%s, %s, %s)"
record1 = "facebook", "daniel1", "wang2"

my_cursor.execute(insertion, record1)
db_connection.commit()