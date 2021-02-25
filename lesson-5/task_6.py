with open('task_6.txt', 'r', encoding='UTF-8') as task:
    result_dict = dict()
    for line in task:
        pos = line.find(':')
        num = ''.join([line[i] for i in range(len(line)) if line[i].isdigit() or line[i] == ' ']).split(' ')
        num_int = [int(el) for el in num if el != '']
        result_dict[line[:pos]] = sum(num_int)
    print(result_dict)
