def cafe_menu():
    """
    Упрощенное интерактивное меню кафе
    """
    print("☕ МЕНЮ КАФЕ")
    print("1 - Кофе (120 руб)")
    print("2 - Чай (80 руб)") 
    print("3 - Сок (100 руб)")
    print("4 - Вода (50 руб)")
    print("5 - Какао (90 руб)")
    
    try:
        # Выбор напитка
        choice = input("Выберите напиток (1-5): ").strip()
        
        # Обработка выбора
        match choice:
            case "1":
                drink = "Кофе"
                price = 120
            case "2":
                drink = "Чай" 
                price = 80
            case "3":
                drink = "Сок"
                price = 100
            case "4":
                drink = "Вода"
                price = 50
            case "5":
                drink = "Какао"
                price = 90
            case _:
                print("Ошибка: выберите номер от 1 до 5")
                return
        
        # Количество порций
        quantity = int(input("Количество порций: "))
        
        # Расчет суммы
        total = price * quantity
        
        # Склонение слова "порция"
        if quantity == 1:
            portions = "порция"
        elif 2 <= quantity <= 4:
            portions = "порции"
        else:
            portions = "порций"
        
        # Вывод результата
        print("\n=== ВАШ ЗАКАЗ ===")
        print(f"Напиток: {drink}")
        print(f"Цена: {price} руб")
        print(f"Количество: {quantity} {portions}")
        print(f"Сумма: {total} руб")
        print("==================")
        
    except ValueError:
        print("Ошибка: введите корректное число")

# Запуск программы
cafe_menu()
