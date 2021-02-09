ls = list()
# analysis_dict = dict()
title_ls = list()
price_ls = list()
cnt_ls = list()
measure_ls = list()
add = 'да'
i = 1
while add == 'да':
    title = input("Введите название: ")
    price = input("Введите цену: ")
    cnt = input("Введите количество: ")
    measure = input("Введите еденицу измерения: ")
    product_dict = {"название": title,
                    "цена": price,
                    "количество": cnt,
                    "ед.": measure}
    product_tuple = (i, product_dict)
    ls.append(product_tuple)
    i += 1
    add = input("Добавить еще один товар? (да/нет): ")
for n in range(i-1):
    tup = ls[n]
    title_ls.append(tup[1].get("название"))
    price_ls.append(tup[1].get("цена"))
    cnt_ls.append(tup[1].get("количество"))
    measure_ls.append(tup[1].get("ед."))
analysis_dict = {"название": title_ls,
                 "цена": price_ls,
                 "количество": cnt_ls,
                 "ед.": measure_ls}
print()
print("Аналитика товаров:")
for k, v in analysis_dict.items():
    print(f"{k}: {v}")
