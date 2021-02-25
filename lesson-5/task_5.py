from random import randint


with open('task_5.txt', 'w', encoding='UTF-8') as task:
    my_num = [str(randint(0, 1000)) for _ in range(randint(5, 20))]
    task.write(' '.join(my_num))

with open('task_5.txt', 'r', encoding='UTF-8') as task:
    content = task.read()
    num_list = [int(item) for item in content.split(' ')]
    s = sum(num_list)

print('Набор чисел из файла:\n', content)
print('Сумма чисел из файла равна:', s)
