def craete_list():
    print("Введите числа для списка:")
    lis = [int(s) for s in input().split()]
    return lis


def count_denial_elements(x):
    count = 0
    for i in x:
        if int(i) < 0:
            count += 1

    print("Отрицательных чисел: ", count)


c = craete_list()
summ = count_denial_elements(c)