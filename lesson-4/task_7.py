from functools import reduce


def fact(a):
    def multi(perv_el, el):
        return perv_el * el
    for i in range(1, a+1):
        f = reduce(multi, range(1, i+1))
        yield f


n = int(input('Введите n для вывода значений, начиная с 1! и до n!: '))
fact_list = [el for el in fact(n)]
print(f'Значения первых {n} факториалов: \n {fact_list}')
