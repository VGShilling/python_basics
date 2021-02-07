first = float(input("Введите результат пробежки в 1-ый день: "))
target = float(input("Введите резутьтат который нужно достичь: "))
x = first
day = 1
while target >= x:
    x = x + (x / 10)
    day = day + 1
print(f"на {day}-й день спортсмен достиг результата — не менее {target:.0f} км")
