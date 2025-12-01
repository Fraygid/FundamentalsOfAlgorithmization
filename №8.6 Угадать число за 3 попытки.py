secret = int(input('Введите загаданное число: '))
guessed = False

for i in range(1, 4):
    guess = int(input('Введите попытку угадки числа: '))
    if guess == secret:
        print('Угадали!')
        guessed = True
        break
    elif guess < secret:
        print('Не угадали. Число больше')
    else:
        print('Не угадали. Число меньше')

if not guessed:
    print(f'Не угадали за все попытки. Загаданное число: {secret}')
