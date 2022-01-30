from tkinter import *


def SortInc3(event):
    num1 = float(n1.get())
    num2 = float(n2.get())
    num3 = float(n3.get())

    figers = num1, num2, num3
    w = list(figers)
    resault = sorted(w)
    numbers['text'] = "Результат сортировки: " + str(resault).strip('[]')


root = Tk()
root.title("Сортирвка вещественных чисел.")
root.geometry("400x300")

# Создём рамку и помещаем в неё виджеты
Frame_center = Frame()
Frame_center.pack(anchor='center')

Label(Frame_center, text="1-е вещественное число:", font='TimesNewRoman 10').grid(row=0, column=0, padx=5, pady=5)
n1 = Entry(Frame_center)
n1.grid(row=0, column=2, pady=5)

Label(Frame_center, text="2-е вещественное число:", font='TimesNewRoman 10').grid(row=1, column=0, pady=5)
n2 = Entry(Frame_center)
n2.grid(row=1, column=2)

Label(Frame_center, text="3-е вещественное число:", font='TimesNewRoman 10').grid(row=2, column=0, pady=5)
n3 = Entry(Frame_center)
n3.grid(row=2, column=2, pady=5)

button1 = Button(Frame_center, text="Сортировать", relief='raised')
button1.grid(row=3, column=0)

Label(Frame_center, font='TimesNewRoman 10').grid(row=4, column=0, pady=5)

numbers = Label(Frame_center, font='TimesNewRoman 10')
numbers.grid(row=4, column=0, pady=5)

button1.bind("<Button-1>", SortInc3)

root.mainloop()
