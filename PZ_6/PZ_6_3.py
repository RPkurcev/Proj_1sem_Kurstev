# Список имеет размер N. Нужно осуществить сдвиг элементов списка влево на одну позицию,
# при этом исходное значение первого элемента будет утеряно. Также последний элемент полученного списка
# положить равны 0.


s = int(input("Введите дипазон списка.\n"
              "Введите 1-ое число диапозона: "))
e = int(input("Введите 2-ое число диапозона: "))
A = list(range(s, e))
print("Исходный список A = ", A)

k = 0
b = 1
while b < len(A):
    A[k] = A[b]
    while b < len(A):
        b += 1
        k += 1
        break
A[-1] = 0
print("Конечный список A = ", A)
