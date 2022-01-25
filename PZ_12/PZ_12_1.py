import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x500')

background_image = PhotoImage(file='background.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0)

Frame_center = Frame(bg='light grey')  # Устанавливаем рамку
Frame_center.pack(anchor='center')

Label(Frame_center, bg='light grey', text="First Name", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, 'Jim')  # Благодаря insert можно поместить текст
textExample.pack(anchor='s', ipady=5)

Label(Frame_center, bg='light grey', text="Last Name", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, 'Smith*')
textExample.pack(anchor='s', ipady=5)

Label(Frame_center, bg='light grey', text="Email", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, 'Email address')
textExample.pack(anchor='s', ipady=5)

Label(Frame_center, bg='light grey', text="Website", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, 'www.example.com')
textExample.pack(anchor='s', ipady=5)

Label(Frame_center, bg='light grey', text="Password", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, '8-10 characters')
textExample.pack(anchor='s', ipady=5)

Label(Frame_center, bg='light grey', text="Password Confirmation", font='TimesNewRoman').pack(anchor='w', ipady=10)

textExample = Entry(Frame_center, width=30, fg='grey')
textExample.insert(END, 'Type your password again')
textExample.pack(anchor='s', ipady=5)

Button(Frame_center, width=6, relief='raised', height=1, bg='light grey', text="Sign Up", font='TimesNewRoman')\
    .pack(anchor='w', ipady=5)

root.mainloop()
