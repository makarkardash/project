def calculate_area(length, width):
    return length * width

length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

area = calculate_area(length, width)

print("Площадь прямоугольника равна:", area)