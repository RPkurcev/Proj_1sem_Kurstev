import sqlite3 as sq
import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = db
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD_11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="Search.gif")
        btn_search = tk.Button(toolbar, text="Командировачные расходы", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

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

    def records(self, user_id, name, sex, old, score):
        self.db.insert_data(user_id, name, sex, old, score)
        self.view_records()

    def search_travel_expense(self, second_name):
        second_name = (second_name,)
        self.db.cur.execute("""SELECT * FROM travel_expenses WHERE second_name = ? """, second_name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_order = tk.Label(self, text='№ приказа')
        label_order.place(x=50, y=25)
        self.entry_order = ttk.Entry(self)
        self.entry_order.place(x=110, y=25)

        label_name = tk.Label(self, text='Фамилия')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_sex = tk.Label(self, text='Место командировки')
        label_sex.place(x=50, y=75)
        self.entry_name = ttk.Entry(self)
        self.combobox.place(x=110, y=75)

        label_old = tk.Label(self, text='Возраст')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        label_score = tk.Label(self, text='Результат')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()


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

    def insert_data(self, user_id, name, sex, old, score):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)""",
                         (user_id, name, sex, old, score))
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
