num = int(input("Введите целое положительное число: "))
n_max = 0
while num > 0:
    n = num % 10
    if n > n_max:
        n_max = n
    num = num // 10
print(n_max)
