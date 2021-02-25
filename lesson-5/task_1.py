with open('task_1.txt', 'w', encoding='UTF-8') as task:
    string = ' '
    print('Запишите построчно данные:\n(пустая строка - окончание ввода)')
    while string != '':
        string = input(':')
        task.writelines(string+'\n')
