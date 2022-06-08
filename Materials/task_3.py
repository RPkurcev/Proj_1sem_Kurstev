def craete_lists():
    print("Введите числа для 1-го списка:")
    lis = [int(s) for s in input().split()]

    print("Введите числа для 2-го списка:")
    lis_2 = [int(s) for s in input().split()]

    lis_3 = [lis] + [lis_2]
    return lis, lis_2, lis_3


def count_denial_elements(x):
    s = sum(list(x))
    print("Сумма: ", s)


c = craete_lists()
summ = count_denial_elements(c)
