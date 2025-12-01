num=int(input('Введите число с которым вам нужно сделать таблицу умножения: '))

for i in range(1, 11):
    print(f'{num}*{i} = {num*i}')
