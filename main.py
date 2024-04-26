# Все правки были сделаны чтобы код соответсвовал Т/З
# Список правок:
# Неправильно составлены вычисления в функциях и из-за этого выдавался неправильный результат
# Добавлена возможность вводить значения соотношения в произвольном порядке
# Исправлены вычисления в функции нахождения соотношения сторон
# Ну короче плохо, крайне плохо. Я думал проблемы будут только в нахождении соотношения сторон, а они возникли вообще везде.
# Плохо учишься
from math import gcd
def find_smaller_side():
    larger_side = int(input("Введите большую сторону: "))
    ratio1 = int(input("Введите первое значение соотношения: "))
    ratio2 = int(input("Введите второе значение соотношения: "))
    if ratio1 > ratio2:
        smaller_side = (larger_side / ratio1) * ratio2
    else:
        smaller_side = (larger_side / ratio2) * ratio1
    print(f"Меньшая сторона равна: {smaller_side}")

def find_bigger_side():
    smaller_side = int(input("Введите меньшую сторону: "))
    ratio1 = int(input("Введите первое значение соотношения: "))
    ratio2 = int(input("Введите второе значение соотношения: "))
    if ratio1 > ratio2:
        bigger_side = (smaller_side / ratio2) * ratio1
    else:
        bigger_side = (smaller_side / ratio1) * ratio2
    print(f"Большая сторона равна: {bigger_side}")

def find_ratio():
    side1 = int(input("Введите первую сторону: "))
    side2 = int(input("Введите вторую сторону: "))
    if side1 > side2:
        nod = gcd(side1, side2) # Функция gcd находит НОД двух чисел
        ratio = str(side1 // nod) + ":" + str(side2 // nod)
    else:
        nod = gcd(side2, side1)
        ratio = str(side2 // nod) + ":" + str(side1 // nod)
    print(ratio)

choice = int(input("Выберите действие (1 - найти меньшую сторону, 2 - найти большую сторону, 3 - найти соотношение сторон): "))

if choice == 1:
    find_smaller_side()
elif choice == 2:
    find_bigger_side()
elif choice == 3:
    find_ratio()
else:
    print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")