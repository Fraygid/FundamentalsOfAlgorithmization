num = int(input('Введите стартовое количество организмов: '))
plus = int(input('Введите среднесуточное увеличение в процентах: '))
days = int(input('Введите количетсво дней для размножения: '))

for day in range(1, days+1):
    print(f'День:{day}, Размер популяции:{round(num, 0)}')
    num = num + num * plus / 100
