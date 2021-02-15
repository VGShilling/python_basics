def my_func(a):
    i = 0
    s = 0
    total = 0
    while i != '#':
        ls = a.split(' ')
        if ls[-1] == '':
            ls.pop(-1)
        for i in ls:
            if i != '#':
                s += float(i)
            else:
                print('Введен специальный символ #, выполнение программы завершено')
                break
        total += s
        s = 0
        if i == '#':
            break
        print(f'Сумма введенных чисел: {total}')
        a = input('# - завершить. Или продолжите ввод: ')
    return total


string = input('Введите строку чисел, разделенных пробелом: ')
print(f'Сумма введенных чисел: {my_func(string)}')
