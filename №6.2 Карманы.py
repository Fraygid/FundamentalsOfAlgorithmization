pocket=int(input('Введиет число кармана(0-36): '))

if pocket < 0 or pocket > 36:
    print('Введено некореткное число для кармана')
elif pocket == 0:
    print('Карман зелёный')
elif 1<=pocket<=10:
    if pocket % 2 == 1: #нечетный
        print('Карман красный')
    else: #четный
        print('Карман черный')
elif 11<=pocket<=18:
    if pocket % 2 == 1: #нечетный
        print('Карман черный')
    else: #четный
        print('Карман красный')
elif 19<=pocket<=28:
    if pocket % 2 == 1: #нечетный
        print('Карман красный')
    else: #четный
        print('Карман черный')
else: #29<=pocket<=36
    if pocket % 2 == 1: #нечетный
        print('Карман черный')
    else: #четный
        print('Карман красный')
