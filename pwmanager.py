import sqlite3
from tkinter import *
from cryptography.fernet import Fernet

conn = sqlite3.connect('pwmanager.db')
c = conn.cursor() 

# c.execute("""CREATE TABLE passwords (
#         website text,
#         username text,
#         password text
#     )""")

root = Tk()
root.title('Password Manager')
root.geometry("400x600")

file = open('key.txt', 'rb')
key = file.read() # key is in bytes
file.close()


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
    text_label.grid(row=13, column=0, columnspan=2)
    i = 14

    for item in items:
        # decrypt password
        f2 = Fernet(key)
        decrypted = f2.decrypt(item[2])
        # decode
        original_password = decrypted.decode()

        entry = item[0] + "     " + item[1] + "     " + original_password + "\n"
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

    # encrypt password
    
    # encode password
    message = password_input
    encoded = message.encode()

    # encrypt password
    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    c.execute("INSERT INTO passwords VALUES (:website, :username, :password)", 
            {
                'website': website_input,
                'username': username_input,
                'password': encrypted, # encrypted as bytes
            }
    )
    conn.commit()
    conn.close()

    # clear text boxes
    website_field.delete(0, END)
    username_field.delete(0, END)
    password_field.delete(0, END )

# Show one particular record
def show_one():
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()

    retrieve_input = retrieve_field.get()

    c.execute("SELECT * FROM passwords WHERE website = (?)", (retrieve_input,))
    items = c.fetchall()
    for item in items:

        # decrypt password
        f2 = Fernet(key)
        decrypted = f2.decrypt(item[2])
        # decode
        original_password = decrypted.decode()


        entry = item[1] + "     " + original_password + "\n"
        entry_label = Label(root, text=entry)
        entry_label.grid(row=8, column=0, columnspan=4, ipadx=100)
    conn.commit()
    conn.close()

    retrieve_field.delete(0, END)

# Delete record from table
def delete_one():
    conn = sqlite3.connect('pwmanager.db')
    c = conn.cursor()

    delete_input = delete_field.get()

    c.execute("DELETE from passwords WHERE website = (?)", (delete_input,))
    conn.commit()
    conn.close()

    delete_field.delete(0, END)

# Create welcome box
welcome_msg = "Welcome.\nPlease enter your username and password below,\nand the website you are using these credentials with."
welcome_label = Label(root, text=welcome_msg)
welcome_label.grid(row=0, column=0, padx=10, pady=20, columnspan=2)

# Create text boxes
website_field = Entry(root, width=30)
website_field.grid(row=1, column=1, padx=20)

username_field = Entry(root, width=30)
username_field.grid(row=2, column=1, padx=10)

password_field = Entry(root, width=30)
password_field.grid(row=3, column=1, padx=10)

# Create text box labels
website_label = Label(root, text="Website")
website_label.grid(row=1, column=0)

username_label = Label(root, text="Username")
username_label.grid(row=2, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=3, column=0)

# Create submit button
submit_button = Button(root, text="Add record to password manager", command=add_one)
submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create white box
white_box = Label(root, text="\n").grid(row=8, column=0)

# # Create a query button to show all records
query_button = Button(root, text="Show all logins", command=show_all)
query_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a button to retrieve a particular record
retrieve_label = Label(root, text="Enter website to retrieve credentials for")
retrieve_label.grid(row=5, column=0, columnspan=2, pady=10)
retrieve_field = Entry(root, width=30)
retrieve_field.grid(row=6, column=0, columnspan=2)
retrieve_button = Button(root, text="Retrieve login for this website", command=show_one)
retrieve_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Create a button to delete a particular record
delete_label = Label(root, text="Enter website to DELETE credentials for")
delete_label.grid(row=9, column=0, columnspan=2, pady=10)
delete_field = Entry(root, width=30)
delete_field.grid(row=10, column=0, columnspan=2)
delete_button = Button(root, text="DELETE login for this website", command=delete_one)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

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