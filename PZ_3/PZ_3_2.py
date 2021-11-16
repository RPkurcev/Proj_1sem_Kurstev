# Описание вида числа (чётность и разряд числа)
while True:
    value = (input("Введите число в диапозоне от 1 до 999: "))

    while type(value) != int:  # Обработка исключений
        try:
            value = int(value)
        except ValueError:
            print("Введено неправельное значение!")
            value = (input("Введите число в диапозоне от 1 до 999: "))

    if value <= 0:
        print("Введите число согласно диапозону!")
        continue
    elif value >= 1000:
        print("Введите число согласно диапозону!")
        continue

    if 100 <= value <= 999:  # Проверка на трёхзначность числа
        if value % 2 == 0:
            print("Число чётное трёхзначное")
            break
        else:
            print("Число нечётное трёхзначное")
            break
    elif 10 <= value <= 99: # Проверка на двузначность числа
        if value % 2 == 0:
            print("Число чётное двузначное")
            break
        else:
            print("Число нечётное двузначное")
            break
    elif 1 <= value <= 9:  # Проверка на однозначность
        if value % 2 == 0:
            print("Число чётное однозначное")
            break
        else:
            print("Число нечётное однозначное")
            break
