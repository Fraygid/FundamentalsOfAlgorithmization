num = int(input('Введите натуральное число(больше 2): '))

first = -1
second = -1

if num < 2:
    print('Число должно быть больше 2')
else:
    for i in range(num):
        x = int(input(f'Введите число №{i+1}: '))
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x
    print(f'Наибольшее число: {first}')
    print(f'Второе по величине: {second}')
