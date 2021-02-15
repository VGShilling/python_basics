def user_inf(name, surname, year, city, email, phone):
    user_data = ' '.join([name, surname, year, city, email, phone])
    return user_data


data = list()
key = ("имя", "фамилию", "год рождения", "город проживания", "email", "телефон")
for i in range(6):
    data.append(str(input(f'Введите {key[i]}: ')))
print('Данные пользователя:')
print(user_inf(name=data[0], surname=data[1], year=data[2], city=data[3], email=data[4], phone=data[5]))
