print('Введите имена участников (для завершения напишите "конец")')

count = 0
found_alexandra = False
between_count = 0

while True:
    name = input('Введите имя участника: ')

    if name == 'конец':
        break

    if name == 'Александра':
        found_alexandra = True
        continue

    if name == 'Левон':
        break

    if found_alexandra:
        between_count += 1
print(f'Между Александрой и Левоном находится {between_count} человек(а).')
