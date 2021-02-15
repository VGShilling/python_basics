def division(a, b):
    return a/b


while True:
    try:
        num1 = int(input('Ведите числитель: '))
        num2 = int(input('Введите знаменатель: '))
        print(f'{num1} / {num2} = {division(num1, num2)}')
        break
    except ValueError:
        print("<<< ERROR!!!: Введите число >>>")
    except ZeroDivisionError:
        print("<<< ERROR!!!: Введите знаменатель > 0 >>>")
