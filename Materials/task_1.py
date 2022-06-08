def craete_list():
    print("Введите числа для списка:")
    lis = [int(s) for s in input().split()]
    return lis


def add_elements(x):
    s = sum(list(x))
    print("Сумма: ", s)


c = craete_list()
summ = add_elements(c)

