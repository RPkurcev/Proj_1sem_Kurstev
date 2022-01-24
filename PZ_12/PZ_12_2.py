from tkinter import *


def SortInc3(event):
    num1 = float(n1.get())
    num2 = float(n2.get())
    num3 = float(n3.get())

    z = num1, num2, num3
    w = list(z)
    resault = sorted(w)
    numbers['text'] = * "Порядок чисел", * resault


root = Tk()
root.title("Сортирвка вещественных чисел.")
root.geometry("600x400")

Label(text="1-е вещественное число:").grid(row=0, column=0)
n1 = Entry()
n1.grid(row=0, column=2)

Label(text="2-е вещественное число:").grid(row=1, column=0)
n2 = Entry()
n2.grid(row=1, column=2)

Label(text="3-е вещественное число:").grid(row=2, column=0)
n3 = Entry()
n3.grid(row=2, column=2)

button1 = Button(text="Сортировать")
button1.grid(row=3, column=0)

numbers = Label()
numbers.grid(row=3, column=2)

button1.bind("<Button-1>", SortInc3)

root.mainloop()