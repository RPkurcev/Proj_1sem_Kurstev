# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл

import re

with open("Dostoevsky.txt", 'r', encoding='utf-8') as file:
    text = file.read()
    for p in re.finditer(r'1857 год', text):
        print(p[0])
        for z in re.finditer(r'\w+', text):
            print(z[0])
            if z == '1860–1866 гг.':
                break