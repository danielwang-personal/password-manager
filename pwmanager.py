import sqlite3

# Query the databse and return ALL records
def show_all():
    # Connect to databse and create cursor
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM passwords")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()


# Add a new record to the table
def add_one(website,username,password):
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?,?,?)", (website, username, password))
    conn.commit()
    conn.close()

# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()
    c.execute("DELETE from passwords WHERE rowid = (?)", id)
    conn.commit()
    conn.close()



# CREATE A TABLE
# c.execute("""CREATE TABLE passwords (
#         website text,
#         username text,
#         password text
#     )""")

# DROP TABLE
# c.execute("DROP TABLE passwords")

# conn.commit()
# INSERT INTO TABLE
# c.execute("INSERT INTO passwords VALUES ('Google', 'jack3', 'password123')")

# UPDATE RECORDS
# c.execute("""UPDATE passwords SET username = 'jack@gmail.com'
#             WHERE rowid = 2
#     """)

# conn.commit()

# DELETE RECORDS
# c.execute("DELETE from passwords WHERE rowid = 3")
# conn.commit()

# QUERY THE DATABASE
# c.execute("SELECT rowid, * FROM passwords ORDER BY rowid DESC")
# c.execute("SELECT rowid, * FROM passwords WHERE username LIKE 'dan%'")
# items = c.fetchall()

# for item in items:
#     print(item)

# # COMMIT THE COMMAND
# conn.commit()

# # CLOSE CONNECTION
# conn.close()