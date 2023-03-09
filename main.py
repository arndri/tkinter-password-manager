from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search():
    value = in1.get()
    email = ""
    password = ""
    try:
        with open("data.json","r") as f:
            temp1_data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found",message="No Data File Found")
    else:
        if value in temp1_data:
            email = temp1_data[value]["email"]
            password = temp1_data[value]["password"]
            messagebox.showinfo(title="Found !",message=f"Website : {value}\nEmail : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Data Not Found",message="The data you are looking for is not in the file")
            in1.delete(0,END)


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
    
    new_data = {
        website:{
        "email":email,
        "password":password,
        }
    }
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Error",message="Please enter the email and password")
    else:
        swt = messagebox.askokcancel(title=website,message=f"The details entered : \nEmail: {email}\nPassword: {password}\nIs it correct ?")
        if swt:
            try:
                #Open json file in read mode to load the file
                with open("data.json","r") as data_file:
                    #Put the data into variable
                    data = json.load(data_file)
            #If the file is not found, then create and dump the new_data
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4) 

            else:
                #Update the data with new data
                data.update(new_data)
                #Open json file in write mode to dump the updated data to the json file
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                in1.delete(0,END)
                in3.delete(0,END)

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
src_btn = Button(text="Search",width=20,command=search)


label1.grid(column=0,row=1)
label1.focus()
label2.grid(column=0,row=2)
label3.grid(column=0,row=3)
in1.grid(column=1,row=1,columnspan=2)
in2.grid(column=1,row=2,columnspan=2)
in2.insert(0,"andri@gmail.com")
in3.grid(column=1,row=3,columnspan=2)
generate_pass_btn.grid(column=2,row=4)
add_btn.grid(column=1,row=4)
src_btn.grid(column=1,row=5,columnspan=2)
window.mainloop()