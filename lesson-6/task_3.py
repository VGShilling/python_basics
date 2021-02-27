class Worker:
    wage_bonus = {'рабочий': {'wage': 50000, 'bonus': 3000},
                  'уборщица': {'wage': 30000, 'bonus': 1000},
                  'секретарь': {'wage': 35000, 'bonus': 1500},
                  'прораб': {'wage': 90000, 'bonus': 5000},
                  'директор': {'wage': 900000, 'bonus': 100000}}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = Worker.wage_bonus.get(self.position)


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        print(f"Доход с учетом премии: {self._income.get('wage') + self._income.get('bonus')}")


pos_1 = Position("Василий", "Прорабов", "прораб")
pos_1.get_full_name()
pos_1.get_total_income()
print(pos_1._income)

pos_2 = Position("Петр", "Боссович", "директор")
pos_2.get_full_name()
pos_2.get_total_income()
print(pos_2.position)

print(Worker.wage_bonus)
