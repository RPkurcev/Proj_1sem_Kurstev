# Дана строка содержащяя полное имя файла. Выделить из этой строки название первого католога
# (без символа "\"), если файл содержится в корневом каталоге, то вывесть символ "\"
name_f = r'C:\Users\Student\PycharmProjects\POKS-22'

name_f1 = name_f[3:] # Этим срезом убераем C:\, так как это будет мешать при итерации.
d = 0
for el in name_f1:
    while d < 1: # C помощью цикла слово выведится один раз.
        d += 1
        if "\\" in name_f1: # C помощью условия выясняем, что есть каталог.
            for el in name_f1:
                if el == '\\':
                    break
                print(el, end='')
        else:
            print('\\ - файл в корневом каталоге.')
