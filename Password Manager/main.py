from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for _ in range(randint(10, 12))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email_id = email_input.get()
    password = password_input.get()

    new_data = {website: {"email": email_id, "password": password}}

    if len(email_id) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Error", message="Required filed cannot be empty")

    else:
        is_ok = messagebox.askokcancel(title="confirm Email/ Password",
                                       message=f"Email id: {email_id}\n password: {password}\n" f"Click OK to save")
        if is_ok:
            try:
                with open("password_data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password_data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("password_data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                messagebox.showinfo(title="Success", message="Your credentials has been successfully saved")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- Search function ------------------------------- #
def search_password():
    data = website_input.get()

    try:
        with open("password_data.json", "r") as data_file:
            password_dict = json.load(data_file)
            email = password_dict[data]["email"]
            password = password_dict[data]["password"]
    except KeyError:
        messagebox.showwarning(title="ERROR", message="Sorry! \nSearch not found")
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="Sorry! \nNo data found")
    else:
        messagebox.showinfo(title=f"Credentials Found for {data}", message=f" Email: {email} \n Password: {password}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
website_text = Label(text="Website:  ")
email_label = Label(text="Email/ Username:  ")
password_label = Label(text="Password:  ")

website_input = Entry(width=32)
email_input = Entry(width=32)
password_input = Entry(width=32)

generate_password = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=43, command=save_password)
search_button = Button(text="Search", width=14, command=search_password)

canvas.grid(column=1, row=0)
website_text.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_input.grid(column=1, row=1)
email_input.grid(column=1, row=2)
password_input.grid(column=1, row=3)
generate_password.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

email_input.focus()
email_input.insert(0, "test@gmail.com")

window.mainloop()
