# Алгоритм должен выводить элементы из списка (список не имеет ограничений) с чётными номерами(индексом).
import random
from random import ran
A = [1, 3, 2, 2, 9]
print("Спиок A = ", A)

z = len(A)
s = 0
k = 2
while s < z:
    print(A[k])
    k += 2