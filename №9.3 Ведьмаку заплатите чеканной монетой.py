price = int(input('Введите цену за услугу ведьмака: '))

coins = [25, 10, 5, 1]
total_coins = 0
remaining_price = price
i = 0

print(f'Цена: {price} крон')
print('Номиналы монет: 1, 5, 10, 25')

while remaining_price > 0 and i < len(coins):
    coin = coins[i]
    if remaining_price >= coin:
        count = remaining_price // coin
        total_coins += count
        remaining_price -= count * coin
        print(f'Монеты номиналом {coin}: {count} шт.')
    i += 1

print(f'Минимальное количество монет: {total_coins}')
