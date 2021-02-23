ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Исходный список: \n', ls)
result_ls = [ls[i+1] for i in range(len(ls)-1) if ls[i] < ls[i+1]]
print('Результат: \n', result_ls)
