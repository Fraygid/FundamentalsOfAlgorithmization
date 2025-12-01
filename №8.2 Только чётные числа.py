print('Введите 10 чисел последовательно через строку')
all_even = True

for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        all_even = False

if all_even:
    print('Да')
else:
    print('Нет')
