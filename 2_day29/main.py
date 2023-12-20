from random import choice,shuffle, random
from tkinter import *
from tkinter import messagebox
from random import randint
import pyperclip


window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# LOGO
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

# SAVE FUNCTION
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()


    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OOps", message="You haven't entered any fields.")
    else:
        response = messagebox.askokcancel(title="Website", message=f"These are the details entered:"
                                                                   f"Email: {email}, Password: {password}")

        if response:

            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# GENERATE

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = "".join([choice(letters) for _ in range(randint(2, 8))])
    password_symbols = "".join([choice(symbols) for _ in range(randint(2, 4))])
    password_numbers = "".join([choice(numbers) for _ in range(randint(2, 4))])

    password = password_letters + password_symbols + password_numbers
    password_list = list(password)  # Eğer listeye çevirmek istiyorsanız, bu satırı ekleyebilirsiniz.

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, 'end')  # Önceki parolayı sil
    password_entry.insert(0, password)
    pyperclip.copy(password)



# WEBSITE
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry=Entry()
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# EMAIL
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry=Entry()
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"kubra_uzan@outlook.com")

# PASSWORD
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry=Entry()
password_entry.grid(row=3, column=1, columnspan=2)

# BUTTONS
generate_button=Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=3)

add_button=Button(text="Add Information", command=save)
add_button.grid(row=4,column=1)



window.mainloop()

