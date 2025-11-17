exchange_rate=float(input('Введите курс доллара к рублю: '))
def convert_usd_to_rub(amount_usd):
    # Конвертация суммы из долларов в рубли по текущему курсу
    return amount_usd * exchange_rate
def main():
    try:
        amount_usd=float(input('Введите сумму в долларах: '))
        amount_rub=convert_usd_to_rub(amount_usd)
        print(f'{amount_usd:,.2f} USD = {amount_rub:,.2f} RUB')
        print(f'Курс: 1 USD = {exchange_rate} RUB')
    except ValueError:
        print('Ошибка: пожалуйста, введите числовое значение.')
if __name__ == '__main__':
    main()
