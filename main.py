from tkinter import *
from tkinter import  messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = False
    user_info = website + " | " + email + " | " + password + "\n"

    if len(website) >0  and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website,message=f"these are the detailes you entered:\n{email}\n,{website}\n{password} is it ok?")

        with open("password.txt", mode="a" ) as passwd:
            passwd.write(user_info)
            website_entry.delete(0,END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="retry", message="Dont leave empty fields")



# ---------------------------- UI SETUP ------------------------------- #]


window = Tk();
window.title("Password manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels

website_label= Label(text="Website:")
website_label.grid(row=1, column=0 )
email_label= Label(text="Email/Username:")
email_label.grid(row=2, column=0 )
password_label= Label(text="Password:")
password_label.grid(row=3, column=0 )


#entries

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row =1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "esmael25@live.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2 )

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()