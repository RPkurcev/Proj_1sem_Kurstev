# Определить в каких магазинах можно приобрести мясо и молоко.

magnit = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
pytorchka = {'мясо', 'молоко', 'соль'}
perecrestok = {'печенье', 'молоко', 'сыр'}

if 'мясо' in magnit:
    if 'молоко' in magnit:
        print("Мясо и молоко можно приобрести в магните.")
if 'мясо' in pytorchka:
    if 'молоко' in pytorchka:
        print("Мясо и молоко можно приобрести в пятёрочке.")
if 'мясо' in perecrestok:
    if 'молоко' in perecrestok:
        print("Мясо и молоко можно приобрести в перекрёстке.")
