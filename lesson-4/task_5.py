from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print('Произведение всех четных чисел от 100 до 1000: \n', reduce(my_func, my_list))
