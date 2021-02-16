import sqlite3
from tkinter import *

root = Tk()
root.title('Password Manager')
root.geometry("400x400")



# Query the databse and return ALL records
def show_all():
    # Connect to databse and create cursor
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()   

    c.execute("SELECT * FROM passwords")
    items = c.fetchall()

    show_passwords = ''
    show_passwords = "WEBSITE ------ USERNAME ----- PASSWORD\n"
    text_label = Label(root, text = show_passwords)
    text_label.grid(row=5, column=0, columnspan=2)
    i = 6

    for item in items:
        entry = item[0] + "     " + item[1] + "     " + item[2] + "\n"
        entry_label = Label(root, text=entry)
        entry_label.grid(row=i, column=0, columnspan=2)
        i += 1    

    
    conn.commit()
    conn.close()


# Add a new record to the table
def add_one():
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()

    website_input = website_field.get()
    username_input = username_field.get()
    password_input = password_field.get()


    c.execute("INSERT INTO passwords VALUES (:website, :username, :password)", 
            {
                'website': website_input,
                'username': username_input,
                'password': password_input,
            }
    )
    conn.commit()
    conn.close()

    # clear text boxes
    website_field.delete(0, END)
    username_field.delete(0, END)
    password_field.delete(0, END )

# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()
    c.execute("DELETE from passwords WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


# Create text boxes
website_field = Entry(root, width=30)
website_field.grid(row=0, column=1, padx=20)

username_field = Entry(root, width=30)
username_field.grid(row=1, column=1, padx=20)

password_field = Entry(root, width=30)
password_field.grid(row=2, column=1, padx=20)

# Create text box labels
website_label = Label(root, text="Website")
website_label.grid(row=0, column=0)

username_label = Label(root, text="Username")
username_label.grid(row=1, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=2, column=0)

# Create submit button
submit_button = Button(root, text="Add record to password manager", command=add_one)
submit_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_button = Button(root, text="Show passwords", command=show_all)
query_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


root.mainloop()





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