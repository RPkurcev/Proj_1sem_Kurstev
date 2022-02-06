from functools import reduce
import math

# В последовательности на n целых чисел найти и вывести:
#   1.минимальный среди положительных
#   2.элемнты кратные пяти
#   3.их среднеее арифметическое

# Находим минимальный среди положительных
numbers = [12, -3, 2, -6, 8, -1, 57, 3, 20]
positive_numbers = list(filter(lambda x: x > 0, numbers))
positive_numbers_2 = str(positive_numbers)
print('Список положительных чисел:', positive_numbers_2.strip('[]'))
print("Минимальное положительное число:", min(positive_numbers), '\n')

# Находим элемнты кратные пяти
f_list = str(numbers)
print('Исходный список:', f_list.strip('[]'))
print("Числа кратные 5:", *list(filter(lambda x: x % 5 == 0, numbers)), '\n')

# Находим среднеее арифметическое списка
middle_number = reduce(lambda x, y: x + y, numbers)
number = middle_number / len(numbers)
print("Среднеее арифметическое число списка =", round(number, 3))
