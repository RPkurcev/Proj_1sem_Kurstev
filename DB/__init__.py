import sqlite3 as sq

with sq.connect('../PZ_16/travel_expenses.db') as con:
    cur = con.cursor()

    cur.execute(("""CREATE TABLE IF NOT EXISTS  travel_expenses(
                number_order INTEGER PRIMARY KEY AUTOINCREMENT,
                second_name  TEXT NOT NULL,
                place_trip TEXT NOT NULL,
                payment REAL,
                advance REAL,
                type_expense TEXT,
                total_expense REAL NULL
                )"""))

    order = '3'

    cur.execute("""SELECT * FROM travel_expenses""")


