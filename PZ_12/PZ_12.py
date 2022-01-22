from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x400')


def close():
    root.destroy()
    root.quit()


label1 = Label(text='Contact us', fg='white', bg='black')
label1.pack()
name_label = Label(text="First Name")
surname_label = Label(text="Last Name")
name_label.grid(row=0, column=0, sticky='n')
surname_label.grid(row=1, column=0, sticky='n')
button1 = ttk.Button(root, text='sign up')
button1.pack()
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
