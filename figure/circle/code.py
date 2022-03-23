def circle_perimetr(default_radius=int(5)):
    radius = int(input("Радиус: "))
    if radius == "":  # Если пользоваетель ничего не вёл
        radius = default_radius
    print("Периметр окружности =", round(float(2 * 3.14 * radius), 3))


def circle_area(default_radius=5):
    radius = int(input("Радиус: "))
    if radius == "":
        radius = default_radius
    print("Периметр окружности =", round(float(2 * 3.14 * default_radius), 3))
