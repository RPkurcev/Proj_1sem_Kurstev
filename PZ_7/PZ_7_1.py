# Дана строка S. Нужно вывести строку, содержащую символы строки S между, которыми  вставлено
# по одному пробелу.

S = 'asdjfj'
z = 0
for el in S:
    print(S[z] + ' ', end='')
    z += 1
