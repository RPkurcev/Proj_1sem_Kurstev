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


    cur.execute("""SELECT * FROM travel_expenses WHERE second_name = "Иванов" """)

    resault = cur.fetchall()

    print(resault)
