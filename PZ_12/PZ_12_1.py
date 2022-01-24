from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x600')

imag = PhotoImage(file='square.png')
l = Label(image=imag).grid()

Label(text="First Name").grid(row=0, column=0)
Entry().grid(row=1, column=0)

Label(text="Last Name").grid(row=2, column=0)
Entry().grid(row=3, column=0)

Label(text="Email").grid(row=4, column=0)
Entry().grid(row=5, column=0)

Label(text="Website").grid(row=6, column=0)
Entry().grid(row=7, column=0)

Label(text="Password").grid(row=8, column=0)
Entry().grid(row=9, column=0)

Label(text="Password Confirmation").grid(row=10, column=0)
Entry().grid(row=11, column=0)

Button(text="Sign Up").grid(row=12, column=0)
root.mainloop()
