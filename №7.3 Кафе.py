coffee_price = 120
tea_price = 80
juice_price = 100
water_price = 50
lemonade_price = 90

print("Добро пожаловать в кафе!")
print("Наше меню:")
print("1 - Кофе - 120 рублей")
print("2 - Чай - 80 рублей")
print("3 - Сок - 100 рублей")
print("4 - Вода - 50 рублей")
print("5 - Лимонад - 90 рублей")
print()


drink_input = input("Введите номер напитка (1-5): ")
quantity_input = input("Введите количество порций: ")
discount_input = input("Введите код скидки (если нет, нажмите Enter): ")


if not drink_input.isdigit() or not quantity_input.isdigit():
    print("Ошибка: номер напитка и количество должны быть числами")
else:
    drink_number = int(drink_input)
    quantity = int(quantity_input)


    if drink_number < 1 or drink_number > 5:
        print("Ошибка: номер напитка должен быть от 1 до 5")
    elif quantity <= 0:
        print("Ошибка: количество должно быть больше 0")
    else:
        if drink_number == 1:
            drink_name = "Кофе"
            price = coffee_price
        elif drink_number == 2:
            drink_name = "Чай"
            price = tea_price
        elif drink_number == 3:
            drink_name = "Сок"
            price = juice_price
        elif drink_number == 4:
            drink_name = "Вода"
            price = water_price
        else:
            drink_name = "Лимонад"
            price = lemonade_price


        total = price * quantity


        discount = 0
        discount_percent = 0


        if discount_input.upper() == "STUDENT":
            discount_percent = 20
            discount = total * discount_percent / 100
            final_total = total - discount
        else:
            final_total = total


        if quantity == 1:
            portion_word = "порция"
        elif 2 <= quantity <= 4:
            portion_word = "порции"
        else:
            portion_word = "порций"


        print()
        print("=" * 30)
        print("        КВИТАНЦИЯ КАФЕ")
        print("=" * 30)
        print(f"Товар: {drink_name}")
        print(f"Цена за порцию: {price} руб")
        print(f"Количество: {quantity} {portion_word}")
        print(f"Сумма: {total} руб")
        print()


        if discount > 0:
            print(f"Скидка '{discount_input}' ({discount_percent}%): {discount:.0f} руб")

        print("=" * 30)
        print(f"К ОПЛАТЕ: {final_total:.0f} руб")
        print("=" * 30)
        print("Спасибо за заказ!")
