def craete_lists():
    print("Введите числа для 1-го списка:")
    lis = [int(s) for s in input().split()]

    print("Введите числа для 2-го списка:")
    lis_2 = [int(s) for s in input().split()]

    return lis, lis_2


def add_elements(x, c):
    s = sum(list(x))
    s_2 = sum(list(c))

    print("Сумма: ", s + s_2)


list_1, list_2 = craete_lists()
summ = add_elements(list_1, list_2)
