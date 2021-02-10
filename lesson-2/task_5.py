my_list = [7, 5, 3, 3, 2]
print(f"Исходные элементы рейтинга: {my_list}")
while True:
    try:
        new_el = abs(int(input("Введите элемент рейтинга (натуральное число): ")))
        break
    except ValueError as err:
        print("ERROR!!!: Введите натуральное число")
my_list.append(new_el)
my_list.sort(reverse=True)
print(my_list)
