def my_func(x, y):
    deg_1 = x**y
    z = x
    for i in range(1, abs(y)):
        z *= x
    deg_2 = 1 / z
    return f"x ^ y = {deg_1}, x ^ y = {deg_2}"


while True:
    try:
        num1 = float(input('Введите действительное положительное число x: '))
        a = 1 / (num1 + abs(num1))
        break
    except ZeroDivisionError:
        print("<<< ERROR!!!: Введите положительное число >>>")
    except ValueError:
        print("<<< ERROR!!!: Введите число >>>")
while True:
    try:
        num2 = int(input('Введите целое отрицательное число y: '))
        b = 1 / (num2 - abs(num2))
        break
    except ZeroDivisionError:
        print("<<< ERROR!!!: Введите отрицательное число >>>")
    except ValueError:
        print("<<< ERROR!!!: Введите число >>>")
print(my_func(num1, num2))
