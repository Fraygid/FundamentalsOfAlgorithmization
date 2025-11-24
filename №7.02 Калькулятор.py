first_number=int(input('Введите первое число: '))
second_number=int(input('Введите второе число: '))
operation=input('Введите операцию(+,-,*,/): ')

match operation:
    case '+':
        result = first_number + second_number
        print(f'Результат сложения: {result}')
    case '-':
        result = first_number - second_number
        print(f'Результат вычитания: {result}')
    case '*':
        result = first_number * second_number
        print(f'Результат умножения: {result}')
    case '/':
        result = first_number / second_number
        print(f'Результат вычисления: {result}')
    case _:
        print('Неизвестная операция')
