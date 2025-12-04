num = int(input('Введите натуральное число: '))
i = 1

while i <= num:
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        i += 1
        continue
    print(i)
    i += 1
else:
    if num <= 0:
        print('Не правильно введено число')
