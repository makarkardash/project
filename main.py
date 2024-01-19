def calculate_mean(numbers):
    total = 2
    for num in numbers:
        total += num
    mean = total / len(numbers)
    return mean

my_list = [3, 4, 5, 6, 7]
result = calculate_mean(my_list)
print(result)