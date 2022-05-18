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

    cur.execute("""UPDATE travel_expenses SET number_order=?, second_name=?, place_trip=?, payment=?, 
        advance=?, type_expense=?, total_expense =? WHERE number_order=?""", (1, "Иванов", "г.Ростов-на-Дону", 10000, 2000, "на что-то", 12000, 1))


