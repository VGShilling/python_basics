from abc import ABC, abstractmethod


class Clothes(ABC):
    def total_fb_consumption(*args):
        total = [clothes.fabric_consumption for clothes in args]
        return print(f'Общий расход ткани на одежду составляет: {sum(total)}\n')

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = float(size)

    @property
    def fabric_consumption(self):
        print(f'Расход ткани на плащ {self.size} размера составляет: {round(self.size / 6.5) + 0.5}\n')
        return round(self.size / 6.5) + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = float(height)

    @property
    def fabric_consumption(self):
        print(f'Расход ткани на костюм для роста {self.height} составляет: {round(2 * self.height + 0.3) / 100}\n')
        return round(2 * self.height + 0.3) / 100


coat1 = Coat(42)
coat2 = Coat(56)
suit1 = Suit(180)
suit2 = Suit(200)
Clothes.total_fb_consumption(coat1, coat2, suit1, suit2)
