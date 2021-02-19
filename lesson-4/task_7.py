from math import factorial


def fact(a):
    for i in range(1, a+1):
        f = factorial(i)
        yield f


n = int(input('Введите n для вывода значений, начиная с 1! и до n!: '))
fact_list = [el for el in fact(n)]
print(f'Значения первых {n} факториалов: \n {fact_list}')
