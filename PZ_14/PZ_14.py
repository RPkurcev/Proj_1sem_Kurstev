# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл

import re


with open("Dostoevsky.txt", 'r', encoding='utf-8') as file:
    text = file.readlines()

    b = False
    strings = []
    for n in text:
        if n == "1857 год \n": # Данный блок условного оператора нужен для поиска нужного блока информации
            b = True
        elif n == "1860–1866 гг.\n":
            b = False

        while b:
            strings += re.findall(r".*", n)
            strings.append("\n")
            break

with open("text_1857.txt", 'a', encoding='utf-8') as f:
    f.writelines(strings)





