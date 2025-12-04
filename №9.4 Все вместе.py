num = int(input('Введите натуральное число: '))
original_number = num

count_3 = 0
last_num = num % 10
count_last_num = 0
even_num = 0
sum_5 = 0
product_7 = 1
has_7 = False
count_0_5 = 0

while num > 0:
    digit = num % 10

    if digit == 3:
        count_3 += 1

    if digit == last_num:
        count_last_num += 1

    if digit % 2 == 0:
        even_num += 1

    if digit > 5:
        sum_5 += digit

    if digit > 7:
        product_7 *= digit
        has_7 = True

    if digit == 0 or digit == 5:
        count_0_5 += 1

    num //= 10

if not has_7:
    product_7 = 1

print(f'Исходное число: {original_number}')
print(f'Количество цифр 3: {count_3}')
print(f'Количество последней цифры({last_num}): {count_last_num}')
print(f'Количество четных цифр: {even_num}')
print(f'Сумма цифр больших 5: {sum_5}')
print(f'Произведение цифр больших 7(если цифр больше 7 нет, выведится 1: {product_7}')
print(f'Количество цифр 0 и 5: {count_0_5}')
