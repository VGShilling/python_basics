ls = list()
item = 0
print('Введите элементы списка:')
print('(Чтобы завершить ввод элементов напишите "end")')
while item != 'end':
    item = input(": ")
    ls.append(item)
ls.pop(-1)
for i in range(1, len(ls), 2):
    ls[i-1], ls[i] = ls[i], ls[i-1]
print(ls)
