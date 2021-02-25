with open('task_4.txt', 'r', encoding='UTF-8') as task:
    content = {line.split(' — ')[0]: line.split(' — ')[1][:-1] for line in task}
    translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    result = {translate.get(el): content.get(el) for el in content.keys()}

with open('task_4_result.txt', 'w', encoding='UTF-8') as result_obj:
    for el in result.items():
        string = ' — '.join(list(el))
        result_obj.writelines(string + '\n')
