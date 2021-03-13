class ComplexNum:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __add__(self, other):
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return ComplexNum(sum_a, sum_b)

    def __mul__(self, other):
        mul_a = (self.a * other.a) + (self.b * other.b * -1)
        mul_b = (self.b * other.a) + (self.a * other.b)
        return ComplexNum(mul_a, mul_b)

    def __str__(self):
        if self.b >= 0:
            return str(f'{self.a} + {self.b}i')
        else:
            return str(f'{self.a} - {abs(self.b)}i')


cn_1 = ComplexNum(1, -1)
cn_2 = ComplexNum(3, 6)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
