import tkinter as tk
from Child import *
from Search import *
from Update import *
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="../PZ_16/BD_11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить игрока', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'sex', 'old', 'score'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('name', text='Имя игрока')
        self.tree.heading('sex', text='Пол игрока')
        self.tree.heading('old', text='Возраст игрока')
        self.tree.heading('score', text='Результат игрока')

        self.tree.pack()

    def records(self, user_id, name, sex, old, score):
        self.db.insert_data(user_id, name, sex, old, score)
        self.view_records()

    def update_record(self, user_id, name, sex, old, score):
        self.db.cur.execute("""UPDATE users SET user_id=?, name=?, sex=?, old=?, score=? WHERE user_id=?""",
                            (user_id, name, sex, old, score, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()

        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

class DB:
    def __init__(self):

        with sq.connect('BD/saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER NOT NULL DEFAULT 1,
                old INTEGER,
                score INTEGER
                )""")

    def insert_data(self, user_id, name, sex, old, score):
        self.cur.execute("""INSERT INTO users(user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)""",
                             (user_id, name, sex, old, score))
        self.con.commit()



if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
