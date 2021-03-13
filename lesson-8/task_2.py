class OwnError(Exception):
    def __init__(self, text):
        self.text = text


def dv(numerator, denominator):
    try:
        if denominator == 0:
            raise OwnError("Ошибка. Знаменатель равен нулю!")
    except ValueError:
        print("Ошибка. Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f'{numerator} / {denominator} = {numerator / denominator}')


dv(10, 0)
