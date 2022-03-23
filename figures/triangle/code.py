__all__ = ["triangle_perimetr", "triangle_area"]


def triangle_perimetr(A=7, B=2, C=8):
    a, b, c = input("Сторона a = "), \
              input("Сторона b = "), \
              input("Сторона c = ")

    if a == '': a = int(A)
    if b == '': b = int(B)
    if c == '': c = int(C)
    print("Периметр треугольника =", int(a) + int(b) + int(c))


def triangle_area(A=7, B=2, C=8):
    a, b, c = input("Сторона a = "), \
              input("Сторона b = "), \
              input("Сторона c = ")

    if a == '': a = int(A)
    if b == '': b = int(B)
    if c == '': c = int(C)

    p = ((int(a) + int(b) + int(c)) / 2)  # Полупериметр
    print(p)
    print("Площадь треугольника =", (p * (p - a) * (p - b) * (p - c)) ** (0.5))
