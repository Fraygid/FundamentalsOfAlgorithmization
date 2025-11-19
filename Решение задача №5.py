first=input('Введите красный, желтый или синий цвет: ')
second=input('Введите красный, желтый или синий цвет: ')

if (first!='красный' and first!='желтый' and first!='синий') or (second!='красный' and second!='желтый' and second!='синий'):
    print('Введен неправильный цвет')
elif (first==second):
    print(f'При смешивании получится {first} цвет')
elif first!='красный' and second!='красный':
    print('При смешивании получится зеленый цвет')
elif first!='желтый' and second!='желтый':
        print('При смешивании получится фиолетовый цвет')
elif first!='синий' and second!='синий':
        print('При смешивании получится оранжевый цвет')
