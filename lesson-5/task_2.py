with open('task_2.txt', 'r', encoding='UTF-8') as task:
    line_cnt = 0
    for line in task:
        line_cnt += 1
        words_in_line = len(line.split(' '))
        print(f' в {line_cnt}-й строке {words_in_line} слов(а)')
    print('Всего количество строк в файле: ', line_cnt)
