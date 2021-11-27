# Алгоритм должен найти элемент из списка A, который наиболее близок к числу R, то есть такой элемент A для
# для которого величина |A-R| является минимальной.

import random
from random import randint

N = int(input("Введите кол-во элементов в списке: "))
R = -3
a = list(range(N))
print("Список a = ", a)

min = 0
t = 0
k = 0
while t < N:
    m = abs(a[k] - R)
    k += 1
    n = abs(a[k] - R)
    k += 1
    min = n if n > m else m
    t += 1
print(min)
