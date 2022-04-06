import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute("""SELECT * FROM users""") # Выбираем всех игроков из таблицы
    result = cur.fetchall()
    print(result)

    cur.execute("""SELECT * FROM users WHERE sex == 2""")  # Выбираем всех игроков женского пола
    result = cur.fetchall()
    print(result)

    cur.execute("""SELECT * FROM users WHERE score < 1000""")  # Выбираем всех игроков у которых результат меньше 1000
    result = cur.fetchall()
    print(result)

    cur.execute("""SELECT * FROM users WHERE score > 1000""")  # Выбираем всех игроков с наилучшим результатом
    result = cur.fetchall()
    print(result)

    cur.execute("""SELECT * FROM users WHERE old 18 BETWEEN 18 AND 20""")  # Выбираем всех игроков с наилучшим результатом
    result = cur.fetchall()
    print(result)
