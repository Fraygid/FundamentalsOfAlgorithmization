def atm():
    DENOMINATION=[5000, 2000, 1000, 500, 200, 100]
    try:
        amount=int(input('Введите сумму для снятия(кратную 100): '))
        if amount%100 != 0:
            print('Ошибка: сумма должна быть кратна 100.')
            quit()
        print(f'Запрошенная сумма {amount} руб.')
        print('Выдаваемые купюры: ')
        remaining_amount=amount
        bills_count={}
        for denomination in DENOMINATION:
            count=remaining_amount//denomination
            if count>0:
                bills_count[denomination]=count
                remaining_amount%=denomination
        for denomination in DENOMINATION:
            if denomination in bills_count:
                print(f'{denomination} руб.: {bills_count[denomination]} шт.')
        if remaining_amount %100!=0:
            print('Сумма выдана полностью.')
    except ValueError:
        print('Ошибка: пожалуйста, введите целое число.')
atm()
