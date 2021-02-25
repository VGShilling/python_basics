from functools import reduce


def my_func(prev_el, el):
    return int(prev_el) + int(el)


with open('task_3.txt', 'r', encoding='UTF-8') as task:
    content = {line.split(' ')[0]: int(line.split(' ')[1][:-1]) for line in task}
    low_salary = [el for el in content.keys() if content.get(el) < 20000]
    print(f'Сотрудники с окладом менее 20 тыс.: \n{low_salary}')
    middle_salary = reduce(my_func, content.values()) / len(content.values())
    print(f'Средняя величина дохода сотрудников: \n{middle_salary:.2f}')
