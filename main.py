from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def to_txt():
    website = in1.get()
    email = in2.get()
    password = in3.get()
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
generate_pass_btn = Button(text="Generate Password",width=20)
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