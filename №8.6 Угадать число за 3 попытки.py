import random

secret = random.randint(1,10)
guessed = False

for i in range(1, 4):
    guess = int(input('Введите попытку угадывания числа(от 1 до 10): '))
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
