month =int(input('Введите порядковый номер месяца: '))

if month>12 or month<=0:
    print('Введенно неверное число')
else:
    if month==2:
        print('В месяце 28 дней')
    elif month in [4, 6 ,9 ,11]:
        print('В месяце 30 дней')
    else:
        print('В месяце 31 день')
