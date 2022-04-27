import tkinter as tk
from tkinter import ttk

class Search(tk.Toplevel):
    """Класс для поискового окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_search()

    def init_search(self):
        self.title('Поиск')
        self.geometry('350x120')
        self.resizable(False, False)
        label_description = tk.Label(self, text='Поиск')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=190, y=50)
        self.btn_ok = ttk.Button(self, text='Поиск')
        self.btn_ok.place(x=110, y=50)
        self.btn_ok.bind('<Button-1>')
        self.grab_set()
        self.focus_set()