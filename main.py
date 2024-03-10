a = int(input())
b = int(input())

a_p = a % 2
b_p = b % 2

if (a % 2) * (b % 2) > (a + b) / 2 :
    print(True)
else:
    print(False)