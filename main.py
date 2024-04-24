def find_smaller_side():
    larger_side = float(input("Введите большую сторону: "))
    ratio1 = float(input("Введите первое значение соотношения: "))
    ratio2 = float(input("Введите второе значение соотношения: "))
    smaller_side = larger_side * ratio1 / (ratio1 + ratio2)
    print(f"Меньшая сторона равна: {smaller_side}")

def find_bigger_side():
    smaller_side = float(input("Введите меньшую сторону: "))
    ratio1 = float(input("Введите первое значение соотношения: "))
    ratio2 = float(input("Введите второе значение соотношения: "))
    bigger_side = smaller_side * (ratio1 + ratio2) / ratio1
    print(f"Большая сторона равна: {bigger_side}")

def find_ratio():
    side1 = float(input("Введите первую сторону: "))
    side2 = float(input("Введите вторую сторону: "))
    ratio = side1 / side2
    print(f"Соотношение сторон равно: {ratio}")

choice = int(input("Выберите действие (1 - найти меньшую сторону, 2 - найти большую сторону, 3 - найти соотношение сторон): "))

if choice == 1:
    find_smaller_side()
elif choice == 2:
    find_bigger_side()
elif choice == 3:
    find_ratio()
else:
    print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")