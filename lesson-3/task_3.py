def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return my_list[0]+my_list[1]


ls = list()
print('Введите 3 числа: ')
for i in range(3):
    ls.append(int(input(f'{i+1}-е: ')))
print(my_func(ls[0], ls[1], ls[2]))
