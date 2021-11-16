# Программа проверяет два числа на одинаковую чётность
while True:
    a = input("Введите первое целое число: ")
    b = input("Введите второе целое число: ")

    while type(a) != int: # Обработка исключений 1-го числа
        try:
            a = int(a)
        except ValueError:
            print("Не то ввели!")
            a = input("Введите первое целое число: ")

    while type(b) != int: # Обработка исключений 2-го числа
        try:
            b = int(b)
        except ValueError:
            print("Не то ввели!")
            b = input("Введите второе целое число: ")

    if a == 0:
        print("Не вводите 0.")
        continue
    elif b == 0:
        print("Не вводите 0.")
        continue


    if a % 2 == 0 and b % 2 == 0:
        print("Два числа чётных.")
        break
    elif a % 2 == 1 and b % 2 == 1:
        print("Два числа нечётных.")
        break
    else:
        print("Два числа имеют разную чётность.")
        break