# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл

import re


with open("Dostoevsky.txt", 'r', encoding='utf-8') as file:
    text = file.readlines()
    b = False
    for n in text:
        if n == "1857 год \n":
            b = True
        elif n == "1860–1866 гг.\n":
            b = False

        while b:
            print(*re.findall(r".*", n))
            break