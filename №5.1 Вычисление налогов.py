def calculate_tax():
    Tax_rate=0.13
    annual_income=float(input("Введите годовой доход: "))
    tax_mount=annual_income*Tax_rate
    net_income=annual_income-tax_mount
    print(f'Годовой доход составляет {annual_income:.2f}$')
    print(f'Сумма налога составляет {tax_mount:.2f}$')
    print(f'Чистый доход составляет {net_income:.2f}$')
calculate_tax()
