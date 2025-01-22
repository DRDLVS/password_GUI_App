from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Verificar datos", "dejaste espacios en blanco")
    else:
        is_ok = messagebox.askokcancel(website, f"Estos son los datos que ingresaste: \nEmail: {username}"
                                                f"\n Password: {password} \n proseguimos con esta informacion?")

        if is_ok:
            open_file = open("password_keeper.txt", "a")
            open_file.write(f"* {website}|{username}|{password}\n")
            open_file.close()

            website_input.delete(0, 'end')
            password_input.delete(0, 'end')





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ********** LABELS *******
#website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#email_username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

#password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ********** BUTTONS *******
#generate password button
generate_password = Button(text="generate_password", command=create_password)
generate_password.grid(column=2, row=3, sticky="EW")

#add button
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# ********** Entrys *******
#website Entrys
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

##email_username Entrys
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2,  sticky="EW")
username_input.insert(0, "diego.rdlvs1@gmail.com")

#password Entrys
password_input = Entry(width=17)
password_input.grid(column=1, row=3, sticky="EW")

# ********** CANVAS *******
# Image import
canvas = Canvas(width=200, height=200)
key_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_photo)
canvas.grid(column=1, row=0)


window.mainloop()