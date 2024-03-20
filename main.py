'''# Написать функцию для подсчёта факториала,
# в качестве аргумента которой будет передаваться число


a = 5
out = 1
for i in range(a):
    out = out * (i + 1)
print(out)

b = 5


def square(n):

    return n ** 2


out_square = square(b)
print(out_square)'''


def fakt(a):
    out = 1
    for i in range(a):
        out = out * (i + 1)
    return out
print(fakt(5))