# Дана строка содержащяя полное имя файла. Выделить из этой строки название первого католога
# (без символа "\"), если файл содержится в корневом каталоге, то вывесть символ "\"
name_f = r'C:\Users\Student\PycharmProjects\POKS-22'

symbol = name_f[1:3]

d = 0
for w in name_f:
    d += 1
    if w == ':':
        d -= 1
        break

for n in name_f:
    if n == ':' and '\\':
        for n in name_f:
            print(n, end='')
            if n == '\\':
                break
