class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def make_order(self, num_cells):
        cells_row = ''
        for i in range(self.cells):
            if (i + 1) % num_cells != 0:
                cells_row += '*'
            else:
                cells_row += '*\n'
        return print(f'Вывод по ячеек {num_cells} в ряд: \n{cells_row}')

    def __add__(self, other):
        sum_cells = self.cells + other.cells
        return Cell(sum_cells)

    def __sub__(self, other):
        if (self.cells - other.cells) > 0:
            return Cell(self.cells - other.cells)
        else:
            print('Разность количества ячеек двух клеток меньше нуля')

    def __mul__(self, other):
        mul_cells = self.cells * other.cells
        return Cell(mul_cells)

    def __truediv__(self, other):
        try:
            div_cells = self.cells / other.cells
            return Cell(div_cells)
        except ZeroDivisionError as err:
            print('Ошибка:', err)

    def __str__(self):
        return str(self.cells)


cell_1 = Cell(8)
cell_2 = Cell(9)
print(cell_1 - cell_2)
Cell.make_order(cell_1, 3)
