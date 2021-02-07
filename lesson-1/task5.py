gain = float(input("Введите размер выручки: "))
costs = float(input("Введите размер издержек: "))
total_profit = gain - costs
if total_profit > 0:
    print("Ваше предприятие прибыльное")
    print(f"Рентабельность {gain / total_profit:.3f}")
    employers = int(input("Введите количество сотрудников: "))
    profit = total_profit / employers
    print(f"Прибыль в расчете на одного сотрудника: {profit}")
elif total_profit == 0:
    print("Ваше предприятие не имеет прибыли")
else:
    print("Ваше предприятие убыточное")
