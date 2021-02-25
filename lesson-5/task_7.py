import json


with open('task_7.txt', 'r', encoding='UTF-8') as task:
    content = task.read().replace('.\n', ' ').split(' ')
    firm_profit = {content[i]: int(content[i+2]) - int(content[i+3]) for i in range(0, len(content)-1, 4)}
    positive_profit = [el for el in firm_profit.values() if el > 0]
    average_profit = dict()
    try:
        average_profit = {'average_profit': sum(positive_profit) / len(positive_profit)}
    except Exception as err:
        print("Все фирмы убыточные. Ошибка:", err)
    result = [firm_profit, average_profit]
with open("task_7.json", "w", encoding='UTF-8') as task_json:
    json.dump(result, task_json)
print('\nПроизведена запись данных в', task_json.name)
