def calculate_bmi():
    print("Enter your weight(kg) and height(m) separated by space: ")
    weight, height = map(float, input().split())
    bmi = weight/(height**2)
    print(f'Your BMI index is {bmi:.1f}')
calculate_bmi()
