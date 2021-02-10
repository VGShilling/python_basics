string = input("Введите строку из нескольких слов, разделённых пробелами:")
ls = string.split()
for ind, el in enumerate(ls, 1):
    print(ind, el[0:10])
