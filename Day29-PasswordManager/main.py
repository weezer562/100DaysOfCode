from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice, randint, shuffle
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

data = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = True

    # Valid value check
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Missing Values", message=f"Please include all required fields.")
        is_valid = False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Save Password:\nWebsite: {website}\nEmail\\"
                                                              f"Username: {email}\nPassword:{password}")

    # Create new entry and add to saved date
    if is_ok:
        new_entry = [website, email, password]
        data.append(new_entry)

        # Save to CSV
        header_names = ['Website', 'Email/Username', 'Password']
        new_data = pd.DataFrame(data)
        new_data.to_csv("passwords", header=header_names, index=False)

        # Clear entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_image)
canvas.grid(column=0, row=0, columnspan=4)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, sticky="e")

website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, sticky="e")

email_entry = Entry(width=43)
email_entry.insert(END, "fakeEmail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky="e")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
