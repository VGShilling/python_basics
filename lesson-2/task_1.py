ls = [1, "строка", 5, 6.55, 7, True]
cnt = 0
while cnt < (len(ls)):
    print(f"{cnt+1}-й элемент списка - {type(ls[cnt])}")
    cnt += 1
