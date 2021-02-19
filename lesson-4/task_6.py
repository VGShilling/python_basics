from sys import argv
from itertools import count
from itertools import cycle
from random import randint


def a_func(start):
    for el in count(int(start)):
        if el == int(start) + 10:
            break
        else:
            yield el


def b_func(ls, end):
    cnt = 0
    for el in cycle(ls):
        if cnt == int(end) or cnt == 50:
            break
        else:
            cnt += 1
            yield el


if len(argv) == 1:
    argv.append('20')
    print(f'Параметр не задан. По умолчанию: {argv[1]}')
else:
    print(f'Вы задали параметр: {argv[1]}')
# --------------Задание a)-------------------
a_result = [elem for elem in a_func(argv[1])]
print('\n************** Задание 6. а) **************\n', a_result)

# --------------Задание b)-------------------
b_list = [randint(1, 16) for _ in range(4)]
print('\n************** Задание 6. б) **************')
print('Начальный список: \n', b_list)
b_result = [elem for elem in b_func(b_list, argv[1])]
print('Повторение элементов начального списка: \n', b_result)
