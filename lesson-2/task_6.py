ls = list()
title_ls = set()
price_ls = set()
cnt_ls = set()
measure_ls = set()
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
    title_ls.add(tup[1].get("название"))
    price_ls.add(tup[1].get("цена"))
    cnt_ls.add(tup[1].get("количество"))
    measure_ls.add(tup[1].get("ед."))
analysis_dict = {"название": list(title_ls),
                 "цена": list(price_ls),
                 "количество": list(cnt_ls),
                 "ед.": list(measure_ls)}
print()
print("Аналитика товаров:")
for k, v in analysis_dict.items():
    print(f"{k}: {v}")
