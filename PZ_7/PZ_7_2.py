# Дана строка содержащая полное имя файла. Выделить из этой строки название первого каталога
# (без символа "\"), если файл содержится в корневом каталоге, то вывести символ "\"
name_f = r'C:\Users\Student\PycharmProjects\POKS-22'

name_f1 = name_f[3:]  # Избавляемся от C:\, так как оно будет мещать при итерации.

d = 0
for el in name_f1:
    while d < 1:  # Цикл позволет вывести слово один раз.
        d += 1
        if '\\' in name_f1:
            for el in name_f1:
                if el == '\\':
                    break
                print(el, end='')
        else:
            print('\\ - имя файла.')
