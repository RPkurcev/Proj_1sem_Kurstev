# Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
# финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
# имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
# Оплата, Аванс, Вид расходов, Сумма расходов.
# БД должна обеспечивать получение информации о командировочных расходах по
# фамилии командированного.


import sqlite3 as sq
import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = db
        self.init_main()
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="edit.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)


        self.search_img = tk.PhotoImage(file="edit_2.png")
        btn_search = tk.Button(toolbar, text="Поиск", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="edit_3.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="edit_4.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.open_delete_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="edit_5.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)



        self.tree = ttk.Treeview(self, columns=('number_order', 'second_name', 'place_trip', 'payment', 'advance',
                                                'type_expense', 'total_expense'), height=15, show='headings')

        self.tree.column('number_order', width=70, anchor=tk.CENTER)
        self.tree.column('second_name', width=180, anchor=tk.CENTER)
        self.tree.column('place_trip', width=140, anchor=tk.CENTER)
        self.tree.column('payment', width=140, anchor=tk.CENTER)
        self.tree.column('advance', width=140, anchor=tk.CENTER)
        self.tree.column('type_expense', width=140, anchor=tk.CENTER)
        self.tree.column('total_expense', width=140, anchor=tk.CENTER)

        self.tree.heading('number_order', text='№ приказа')
        self.tree.heading('second_name', text='Фамилия')
        self.tree.heading('place_trip', text='Место командировки')
        self.tree.heading('payment', text='Оплата')
        self.tree.heading('advance', text='Аванс')
        self.tree.heading('type_expense', text='Вид расхода')
        self.tree.heading('total_expense', text='Сумма расходов')

        self.tree.pack()

    def records(self, number_order, second_name, place_trip, payment, advance, type_expense, total_expense):
        self.db.insert_data(number_order, second_name, place_trip, payment, advance, type_expense, total_expense)
        self.view_records()

    def update_record(self, number_order, second_name, place_trip, payment, advance, type_expense, total_expense):
        self.db.cur.execute("""UPDATE travel_expenses SET number_order=?, second_name=?, place_trip=?, payment=?, 
        advance=?, type_expense=?, total_expense =? WHERE number_order=?""",
                            (number_order, second_name, place_trip, payment, advance, type_expense, total_expense,
                             number_order))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM travel_expenses""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_travel_expense(self, second_name):
        second_name = (second_name,)
        self.db.cur.execute("""SELECT * FROM travel_expenses WHERE second_name = ? """, second_name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self, number_order):
        number_order = (number_order,)
        self.db.cur.execute(f"""DELETE FROM travel_expenses WHERE number_order = ? """, number_order)
        self.view_records()



    def open_dialog(self):
        Child(root, app)

    def open_search_dialog(self):
        Search()

    def open_update_dialog(self):
        Update()

    def open_delete_dialog(self):
        Delete()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)

        btn_search.bind('<Button-1>', lambda event: self.view.search_travel_expense(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x280')
        self.resizable(False, False)

        label_order = tk.Label(self, text='№ приказа')
        label_order.place(x=50, y=25)
        self.entry_order = ttk.Entry(self)
        self.entry_order.place(x=175, y=25)

        label_second_name = tk.Label(self, text='Фамилия')
        label_second_name.place(x=50, y=50)
        self.entry_second_name = ttk.Entry(self)
        self.entry_second_name.place(x=175, y=50)

        label_place = tk.Label(self, text='Место командировки')
        label_place.place(x=50, y=75)
        self.entry_place = ttk.Entry(self)
        self.entry_place.place(x=175, y=75)

        label_payment = tk.Label(self, text='Оплата')
        label_payment.place(x=50, y=100)
        self.entry_payment = ttk.Entry(self)
        self.entry_payment.place(x=175, y=100)

        label_advance = tk.Label(self, text='Аванс')
        label_advance.place(x=50, y=125)
        self.entry_advance = ttk.Entry(self)
        self.entry_advance.place(x=175, y=125)

        label_type_expense = tk.Label(self, text='Вид расхода')
        label_type_expense.place(x=50, y=150)
        self.entry_type_expense = ttk.Entry(self)
        self.entry_type_expense.place(x=175, y=150)

        label_total_expense = tk.Label(self, text='Сумма расходов')
        label_total_expense.place(x=50, y=175)
        self.entry_total_expense = ttk.Entry(self)
        self.entry_total_expense.place(x=175, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=205)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=205)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_order.get(),
                                                                       self.entry_second_name.get(),
                                                                       self.entry_place.get(),
                                                                       self.entry_payment.get(),
                                                                       self.entry_advance.get(),
                                                                       self.entry_type_expense.get(),
                                                                       self.entry_total_expense.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=205)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_order.get(),
                                                                          self.entry_second_name.get(),
                                                                          self.entry_place.get(),
                                                                          self.entry_payment.get(),
                                                                          self.entry_advance.get(),
                                                                          self.entry_type_expense.get(),
                                                                          self.entry_total_expense.get()))
        self.btn_ok.destroy()


class Delete(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_delete()
        self.view = app

    def init_delete(self):
        self.title("Удалить запись")
        self.geometry('400x280')
        self.resizable(False, False)

        label_order = tk.Label(self, text="№ приказа")
        label_order.place(x=50, y=20)

        self.entry_order = ttk.Entry(self)
        self.entry_order.place(x=120, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=200, y=50)

        btn_search = ttk.Button(self, text="Удалить")
        btn_search.place(x=115, y=50)

        btn_search.bind('<Button-1>', lambda event: self.view.delete_records(self.entry_order.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('travel_expenses.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute(("""CREATE TABLE IF NOT EXISTS  travel_expenses(
                number_order INTEGER PRIMARY KEY AUTOINCREMENT,
                second_name  TEXT NOT NULL,
                place_trip TEXT NOT NULL,
                payment REAL,
                advance REAL,
                type_expense TEXT,
                total_expense REAL NULL
                )"""))

    def insert_data(self, number_order, second_name, place_trip, payment, advance, type_expense, total_expense):
        self.cur.execute("""INSERT INTO travel_expenses(number_order, second_name, place_trip, payment, advance, type_expense, total_expense) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                         (number_order, second_name, place_trip, payment, advance, type_expense, total_expense))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Командировачные расходы")
    root.geometry("955x375")
    root.resizable(False, False)
    root.mainloop()
