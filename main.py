from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_lists=[]
    nr_letters = random.randint(7,10)
    nr_symbols = random.randint(2,5)
    nr_numbers = random.randint(1,5)

    totalnr=nr_letters+nr_numbers+nr_symbols
    for n in range(0,nr_letters):
        pass_lists.append(random.choice(letters))
    for n in range(0,nr_symbols):
        pass_lists.append(random.choice(symbols))
    for n in range(0,nr_numbers):
        pass_lists.append(random.choice(numbers))
    random.shuffle(pass_lists)
    passw = "".join(pass_lists)
    in3.insert(0,passw)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def to_txt():
    website = in1.get()
    email = in2.get()
    password = in3.get()
    
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Error",message="Please enter the email and password")
    else:
        swt = messagebox.askokcancel(title=website,message=f"The details entered : \nEmail: {email}\nPassword: {password}\nIs it correct ?")
        if swt:
            txt_file = open("data.txt","a")
            txt_file.write(f"{website},{email},{password} \n")
            txt_file.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)

label1 = Label(text="Website:")
in1 = Entry(width=35)
label2 = Label(text="Email/Username:")
in2 = Entry(width=35)
label3 = Label(text="Password:")
in3 = Entry(width=35)
generate_pass_btn = Button(text="Generate Password",width=20,command=generate)
add_btn = Button(text="Add",width=20,command=to_txt)



label1.grid(column=0,row=1)
label1.focus()
label2.grid(column=0,row=2)
label3.grid(column=0,row=3)
in1.grid(column=1,row=1,columnspan=2)
in2.grid(column=1,row=2,columnspan=2)
in3.grid(column=1,row=3,columnspan=2)
generate_pass_btn.grid(column=2,row=4)
add_btn.grid(column=1,row=4)

window.mainloop()