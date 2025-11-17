def calculate_bmi():
    print("Введите свой вес (кг) и рост (м), разделяя их пробелом: ")
    weight, height = map(float, input().split())
    bmi = weight/(height**2)
    print(f'Ваш индекс ИМТ {bmi:.1f}')
calculate_bmi()
