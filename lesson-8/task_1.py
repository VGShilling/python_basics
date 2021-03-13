from random import randint


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_num(cls, date):
        date_num = ''.join(date.split('-'))
        return int(date_num)

    @staticmethod
    def validation(date):
        if int(date.split('-')[0]) in range(1, 32) and int(date.split('-')[1]) in range(1, 13) \
                and int(date.split('-')[2]) in range(1, 2022):
            print('Валидация прошла успешно')
        else:
            print('Некорректное значение даты')


date_str = f'{randint(1, 31):02}-{randint(1, 12):02}-{randint(1, 2021):04}'
print(date_str)
print(Date.date_to_num(date_str))
Date.validation(date_str)
