# В матрице найти сумму элементов второй половины матрицы.
from functools import reduce

mat = [[24, 432, -43],
       [45, 10, 56],
       [0, 21, -9],
       [34, 112, -500]]

two_half = mat[int(len(mat)/2):] # Определем 2-ую половину матрицы
print(two_half, '\n')

ob = reduce(lambda x, y: x + y, two_half) # Создаём из нескольких вложенных списков один общий список
print(ob, '\n')

print("Cумма элементов второй половины матрицы:", reduce(lambda x, y: x + y, ob))



