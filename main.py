# Import necessary modules from tkinter library
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator
def passwd_gen():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password = []
    for letter in range(1, nr_letters+1):
        password.append(random.choice(letters))

    for i in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    for i in range(1, nr_numbers + 1):
        password += random.choice(numbers)


    random.shuffle(password)

    new_pass = ""

    for char in password:
        new_pass += char
    
    password_entry.insert(0,new_pass)
    
    # End of password generetor
# ---------------------------- SAVE PASSWORD ------------------------------- #
# This function is used to save the entered password to a file
def save_pass():
    # Get the entered email, password and website
    email = email_entry.get()
    password = password_entry.get()
    website = website_entery.get()

    # Check if the website and password fields are filled
    if len(website) < 2 or len(password) < 2  :
        # If not, display a message asking the user to fill all fields
        messagebox.askretrycancel(title="ATTENTION", message="Please Fill All The Gaps")
    else:
        # If all fields are filled, display a confirmation message
        is_ok = messagebox.askokcancel(title="Agree", message=f"These are the details you Entered:\n \n {email} \n {password} \n {website}")
        if is_ok:
            # If the user confirms, save the details to a file
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password} \n")
            # Clear the password and website fields
            password_entry.delete(0,END)
            website_entery.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200,height=200, bg="white", highlightthickness=0)
my_picture = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = my_picture)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ",bg="white")
website_label.grid(column=0, row=1)

website_entery = Entry(width=35)
website_entery.grid(column=1,row=1,columnspan=2)
website_entery.focus()

email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"mbashasolomon@gmail.com")

password_label = Label(text = "Password: ", bg="white")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

gen_btn = Button(text="Generete Password", command=passwd_gen)
gen_btn.grid(column=2,row=3)

add_pass = Button(text="ADD", width=36, command=save_pass)
add_pass.grid(column=1,row=4, columnspan=2)


window.mainloop()