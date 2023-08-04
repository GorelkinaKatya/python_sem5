a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

def f(a, b):
    if b == 1:
        return a
    return a * f(a, b - 1)

print(f(a, b))