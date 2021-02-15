def int_func(a):
    return a.title()


while True:
    try:
        string = input('Ведите строку из слов, разделенных пробелом. Каждое слово из маленьких латинских букв : \n')
        check = ''.join(string.split())
        if (check.isascii() is False) or (check.islower() is False):
            raise ValueError
        break
    except ValueError:
        print("<<< ERROR!!!: Введите слова из маленьких латинских букв >>>")
print(int_func(string))
