class Car:
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.direction = 'прямо'
        self.is_police = False

    def go(self, speed):
        self.speed = int(speed)
        if self.speed > 0:
            print(f'{self.name} разгоняется до {abs(self.speed)} км/ч')
        elif self.speed < 0:
            self.direction = 'назад'
            print(f'У {self.name} включена задняя скорость, едем {self.direction} со скоростью {abs(self.speed)} км/ч')
        else:
            print('что-то не так, стоит')

    def stop(self):
        if self.speed > 0 or self.speed < 0:
            print(f'{self.name} остановился')
        else:
            print(f'{self.name} и не ехал')
        self.speed = 0

    def turn(self, direction):
        self.direction = direction
        if self.speed < 120:
            print(f'{self.name} повернул {self.direction}')
        else:
            print(f'{self.name} улетел в кювет со скоростью {abs(self.speed)} км/ч')
            self.speed = 0
            self.direction = 'стоит в кювете'

    def show_speed(self):
        print(f'текущая скорость {self.name} {abs(self.speed)} км/ч')


class TownCar(Car):
    def go(self, speed):
        self.speed = int(speed)
        if self.speed in range(1, 60):
            print(f'{self.name} разгоняется до {abs(self.speed)} км/ч')
        elif self.speed > 60:
            print(f'{self.name} пытается разогнаться до {abs(self.speed)}км/ч.\n'
                  f'Превышение скорости, снижаем до 60 км/ч')
            self.speed = 60
        elif self.speed < 0:
            self.direction = 'назад'
            print(f'У {self.name} включена задняя скорость, едем {self.direction} со скоростью {abs(self.speed)} км/ч')
        else:
            print('что-то не так, стоит')


class SportCar(Car):
    def turn(self, direction):
        self.direction = direction
        if self.speed < 300:
            print(f'{self.name} повернул {self.direction}')
        else:
            print(f'{self.name} улетел в кювет со скоростью {abs(self.speed)} км/ч')
            self.speed = 0
            self.direction = f'{self.name} стоит в кювете'


class WorkCar(Car):
    def go(self, speed):
        self.speed = int(speed)
        if self.speed in range(1, 40):
            print(f'{self.name} разгоняется до {abs(self.speed)} км/ч')
        elif self.speed > 40:
            print(f'{self.name} пытается разогнаться до {abs(self.speed)}км/ч.\n'
                  f'Превышение скорости, снижаем до 40 км/ч')
            self.speed = 40
        elif self.speed < 0:
            self.direction = 'назад'
            print(f'У {self.name} включена задняя скорость, едем {self.direction} со скоростью {abs(self.speed)} км/ч')
        else:
            print('что-то не так, стоим')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True

    def go(self, speed):
        self.speed = int(speed)
        if self.speed in range(1, 60):
            print(f'{self.name} разгоняется до {abs(self.speed)} км/ч')
        elif self.speed > 60:
            print(f'{self.name} включил сирену и разгоняется до {abs(self.speed)}км/ч')
        elif self.speed < 0:
            self.direction = 'назад'
            print(f'У {self.name} включена задняя скорость, едем {self.direction} со скоростью {abs(self.speed)} км/ч')
        else:
            print('что-то не так, стоим')


lada = TownCar('баклажан', 'Lada')
ferrari = SportCar('красный', 'Ferrari')
kamaz = WorkCar('оранжевый', 'Kamaz')
police = PoliceCar('бело-синий', 'УАЗ')

lada.go(150)
ferrari.go(310)
kamaz.go(20)
police.go(70)

lada.turn('налево')
ferrari.turn('направо')
kamaz.turn('назад')

lada.show_speed()
ferrari.show_speed()
police.show_speed()

lada.stop()
kamaz.stop()

print(kamaz.is_police)
print(police.is_police)
print(ferrari.direction)
print(lada.direction)
