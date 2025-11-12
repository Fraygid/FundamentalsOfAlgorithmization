import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
def calculate_triangle_area(a, b, c):
    p=(a+b+c)/2
    area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area
def main():
    print('Введите координаты трёх точек(через пробел): ')
    print('Точка A: ')
    x1, y1=map(float, input().split())
    print('Точка B: ')
    x2, y2=map(float, input().split())
    print('Точка C: ')
    x3, y3 = map(float, input().split())
    side_ab=calculate_distance(x1, y1, x2, y2)
    side_bc=calculate_distance(x2, y2, x3, y3)
    side_ac=calculate_distance(x3, y3, x1, y1)
    area=calculate_triangle_area(side_ab, side_bc, side_ac)
    print(f'Площадь треугольника: {area:.2f}')
if __name__ == '__main__':
    main()
