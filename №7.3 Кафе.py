def cafe_menu():
    print("=" * 35)
    print("| №  | Напиток       | Цена       |")
    print("=" * 35)
    print("| 1  | Кофе          | 120 рублей |")
    print("| 2  | Чай           | 80 рублей  |")
    print("| 3  | Сок           | 100 рублей |")
    print("| 4  | Вода          | 50 рублей  |")
    print("| 5  | Какао         | 90 рублей  |")
    print("=" * 35)

    prices = {
        1: 120,  #кофе
        2: 80,  #чай
        3: 100,  #сок
        4: 50,  #вода
        5: 90  #какао
    }

    names = {
        1: "Кофе",
        2: "Чай",
        3: "Сок",
        4: "Вода",
        5: "Какао"
    }

    try:
        choice_input = input("Введите номер напитка (1-5) или название: ")

        drink_choice = None
        drink_number = None

        match choice_input:
            case '1' | "кофе" | "Кофе":
                drink_choice = "Кофе"
                drink_number = 1
            case '2' | "чай" | "Чай":
                drink_choice = "Чай"
                drink_number = 2
            case '3' | "сок" | "Сок":
                drink_choice = "Сок"
                drink_number = 3
            case '4' | "вода" | "Вода":
                drink_choice = "Вода"
                drink_number = 4
            case '5' | "какао" | "Какао":
                drink_choice = "Какао"
                drink_number = 5
            case _:
                print("❌ Ошибка: напиток не найден в меню")
                return

        try:
            amount = int(input("Введите количество порций: "))
            if amount <= 0:
                print("❌ Ошибка: количество должно быть положительным числом")
                return
        except ValueError:
            print("❌ Ошибка: введите целое число для количества порций")
            return

        discount_input = input("Введите размер скидки в % (или нажмите Enter для отсутствия скидки): ").strip()
        discount = 0
        if discount_input:
            try:
                discount = int(discount_input)
                if discount < 0 or discount > 100:
                    print("❌ Ошибка: скидка должна быть от 0 до 100%")
                    return
            except ValueError:
                print("❌ Ошибка: введите число для скидки")
                return

        price_per_unit = prices[drink_number]
        total_without_discount = price_per_unit * amount
        discount_amount = total_without_discount * (discount / 100)
        final_total = total_without_discount - discount_amount

        if amount == 1:
            portion = "порция"
        elif 2 <= amount <= 4:
            portion = "порции"
        else:
            portion = "порций"

        print("=" * 30)
        print("☕ КВИТАНЦИЯ КАФЕ")
        print("=" * 30)
        print(f"Товар: {drink_choice}")
        print(f"Цена за порцию: {price_per_unit} рублей")
        print(f"Количество: {amount} {portion}")
        print(f"Сумма без скидки: {total_without_discount} рублей")

        if discount > 0:
            print(f"Скидка: {discount}%")
            print(f"Сумма скидки: {discount_amount} рублей")
            print(f"Итоговая сумма: {final_total:.2f} рублей")
        else:
            print(f"Итоговая сумма: {final_total:.2f} рублей")

        print("=" * 30)
        print(f"💳 К ОПЛАТЕ: {final_total:.2f} рублей")
        print("=" * 30)

    except Exception as error:
        print(f"❌ Произошла ошибка: {error}")
cafe_menu()
