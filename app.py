import pwmanager
from tkinter import *

root = Tk()
root.title('Password Manager')
root.geometry("400x400")

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


# Delete record using rowid as string
# pwmanager.delete_one('3')
# pwmanager.show_all()

# Create submit button
submit_button = Button(root, text="Add record to password manager", command=pwmanager.add_one)
submit_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
root.mainloop()