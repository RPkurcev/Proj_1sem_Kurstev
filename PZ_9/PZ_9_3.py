# Определить в каких магазинах можно приобрести мясо и молоко.

magnit = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
pytorchka = {'мясо', 'молоко', 'соль'}
perecrestok = {'печенье', 'молоко', 'сыр'}

a = {'мясо', 'молоко'}

if magnit & a == a:
    print("Мясо и молоко можно приобрести в магните.")
if pytorchka & a == a:
    print("Мясо и молоко можно приобрести в пятёрочке.")
if perecrestok & a == a:
    print("Мясо и молоко можно приобрести в перекрёстке.")
