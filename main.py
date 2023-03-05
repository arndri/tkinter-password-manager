from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.pack()

window.mainloop()