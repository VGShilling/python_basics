ls = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список: \n', ls)
result_ls = [ls[i] for i in range(len(ls)) if ls[i] not in ls[i+1:] and ls[i] not in ls[:i]]
print('Результат: \n', result_ls)
