__all__ = ["square_perimeter", "square_area"]


def square_perimeter(A=17):
    a = int(input("Сторона: "))
    if a == "":  # Если пользоваетель ничего не вёл
        a = A
    print("Периметр квадрата =", 4 * a)


def square_area(A=17):
    a = input("Сторона: ")
    if a == "":  # Если пользоваетель ничего не вёл
        a = A
    print("Площадь квадрата =", int(a) ** 2)



