while True:
    value = input("Введите двузначное число: ")
    while type(value) != int:  # Обработка исключений.
        try:
            value = int(value)
        except ValueError:
            print("Нужно ввести двузначное число, к примеру 23.")
            value = input("Введите двузначное число: ")

    if value == 0:
        print("Введите другое число! К примеру 20.")
        continue
    elif value // 10 == 0:  # Проверяем двузначность числа.
        print("Нужно ввести двузначное число, к примеру 23.")
        continue

    one = value % 10
    ten = value // 10
    print("Число", value, "имеет десятичный разряд", ten)
    print("Число", value, "имеет единичный разряд", one)
    break
