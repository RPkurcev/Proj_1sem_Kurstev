import string
from string import ascii_letters

# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

text = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

print(f"Исходная строка: {text}")
print("Знаки пунктуации строки:", *set(list(filter(lambda x: x in string.punctuation, text))))
