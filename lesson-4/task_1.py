from sys import argv


def work_salary(time_worked, rate):
    return int(time_worked) * int(rate)


print(f"Ваша зарплата: {work_salary(argv[1], argv[2])}")
