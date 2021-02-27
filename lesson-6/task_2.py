class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.basic_weight = 25
        self.basic_thickness = 5

    def total_weight(self):
        print(f'По заданным атрибутам, масса асфальта, необходимого для покрытия дорожного полотна\n '
              f'составляет: {self.__length * self.__width * self.basic_weight * self.basic_thickness}')


road_1 = Road(1000, 6)
road_1.total_weight()
