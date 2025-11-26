first_num = int(input('Введите число A: '))
second_num = int(input('Введите число B: '))

num = second_num-first_num + 1
first_even = first_num + (first_num % 2)
num_even = (second_num - first_even) // 2 + 1
sum_even = num_even * (2 * first_even + 2 * (num_even - 1)) // 2

first_odd = first_num + 1 - (first_num % 2)
num_odd = (second_num - first_odd) // 2 + 1
sum_odd = num_odd * (2 * first_odd + 2 * (num_odd - 1)) // 2

difference = sum_even - sum_odd

print(f'Разность между суммой четных чисел и суммой нечетных чисел от A до B: {difference}')
