def calculate_area(length, width):
    return length * width

# Вводим значения длины и ширины с клавиатуры
length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

# Вызываем функцию calculate_area и передаем ей значения длины и ширины
area = calculate_area(length, width)

# Выводим площадь прямоугольника на экран
print("Площадь прямоугольника равна:", area)
