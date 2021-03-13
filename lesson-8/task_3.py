class NotDigit(Exception):
    def __init__(self, text):
        self.text = text


ls = list()
s = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
print('Введите элементы списка (число) \n(stop - закончить ввод)')
el = input(':')
while el != 'stop':
    try:
        if el.isalpha() or el.isspace() or any(x for x in s if x in el) or el == '':
            raise NotDigit("Ошибка. Введите число")
    except NotDigit as err:
        print(err)
    else:
        ls.append(el)
    el = input(':')

print(ls)
