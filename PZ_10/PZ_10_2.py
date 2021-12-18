# Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания.
# Сформировать новый файл, в который поместить строку наименьшей длины.
# Вывод содержимого файла

f1 = open('text18-11.txt', 'r', encoding='utf-8')
print(f1.read())
f1.close()

# Подсчёт знаков препинания
sym = 0
for i in open('text18-11.txt', encoding='utf-8'):
    a = list(i)
    for x in a:
        if '!' == x:
            sym += 1
        if ',' == x:
            sym += 1
        if '.' == x:
            sym += 1
print("Количество знаков препинания: ", sym)

# Определяем длину наименьшей строки.
a = 0
s = 0
for i in open('text18-11.txt', encoding='utf-8'):
    m = len(list(i))
    a = min(m, s)
    s = m

# Поиск наименьшей строки и отправка её в файл.
f1 = open('string.txt', 'w')
for i in open('text18-11.txt', encoding='utf-8'):
    if a == len(list(i)):
        f1.writelines(i)
f1.close()

f1 = open('string.txt', 'r')
print("Cтрока наименьшей длины -", f1.read())
f1.close()
