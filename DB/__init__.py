import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    # Выбираем всех игроков из таблицы
    cur.execute("""SELECT * FROM users""")
    result = cur.fetchall()
    print(result)

    # Выбираем всех игроков женского пола
    cur.execute("""SELECT * FROM users WHERE sex == 2""")
    result = cur.fetchall()
    print(result)

    # Выбираем всех игроков у которых результат меньше 1000
    cur.execute("""SELECT * FROM users WHERE score < 1000""")
    result = cur.fetchall()
    print(result)

    # Выбираем всех игроков с наилучшим результатом
    cur.execute("""SELECT * FROM users WHERE score > 1000""")
    result = cur.fetchall()
    print(result)

    # Выбираем всех игроков из таблицы с возрастом 18-20 лет
    cur.execute("""SELECT * FROM users WHERE old BETWEEN 18 AND 20""")
    result = cur.fetchall()
    print(result)





