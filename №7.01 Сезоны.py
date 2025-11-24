month=int(input('Введите номер месяца(1-12): '))

match month:
    case 12|1|2:
        season='Зима'
        emoji='❄️'
    case 3|4|5:
        season='Весна'
        emoji='🌿'
    case 6|7|8:
        season='Лето'
        emoji='☀️'
    case 9|10|11:
        season='Осень'
        emoji='🍂'
    case _:
        print('Ошибка ввода')
print(f'Сейчас {season}{emoji}')
