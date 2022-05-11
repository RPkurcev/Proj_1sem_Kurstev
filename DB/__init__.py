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

    # Изменить возраст 19-летних игроков на 20
    cur.execute("UPDATE users SET old = 20 WHERE old = 19")

    # Всем игрокам, имеющим менее 1000 очков, добавить 300 очков
    cur.execute("UPDATE users SET score = score + 300 WHERE score < 1000")

    # Игрокам достигшим возраста 20 лет добавить 100 очков
    cur.execute("UPDATE users SET score = score + 100 WHERE old = 20")

    # Удалить игроков с результатом менее 1000 очков
    cur.execute("DELETE FROM users WHERE score < 1000")


