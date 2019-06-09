# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Side:
    @staticmethod
    def side(x, y):
        return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


class Triangle(Side):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.ab = self.side(a, b)
        self.bc = self.side(b, c)
        self.ca = self.side(c, a)
    
    def perimetr(self):
        return self.ab + self.bc + self.ca

    # полупериметр - общее обозначение р, думаю, так можно назвать функцию, его вычисляющую
    def p(self):
        return self.perimetr() / 2

    def square(self):
        return math.sqrt(self.p() * (self.p() - self.ab) * (self.p() - self.bc) * (self.p() - self.ca))

    def height(self, x, y):
        return 2 * self.square() / self.side(x, y)


point_a = (0, 0)
point_b = (0, 3)
point_c = (2, 0)
triang = Triangle(point_a, point_b, point_c)
print(triang.perimetr())
print(triang.p())
print(triang.square())
print(triang.height(point_c, point_a))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezy(Side):
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self.ab = self.side(a, b)
        self.bc = self.side(b, c)
        self.cd = self.side(c, d)
        self.da = self.side(d, a)

    def isTrapezy(self):
        if self.side(self._a, self._c) == self.side(self._b, self._d) and (self.ab != self.cd or self.bc != self.da):
            return True
        else:
            return False

    def lengthSide(self, a, b):
        if self.isTrapezy():
            return self.side(a, b)
        else:
            return None

    def perimetr(self):
        if self.isTrapezy():
            return self.ab + self.bc + self.cd + self.da
        else:
            return None

    def square(self):
        if self.isTrapezy():
            return (self.da + self.bc) * math.sqrt(self.ab ** 2 - (self.da - self.bc) ** 2 / 4) / 2
        else:
            return None


point_a = (0, 0)
point_b = (1, 2)
point_c = (3, 2)
point_d = (4, 0)
trap = Trapezy(point_a, point_b, point_c, point_d)
if trap.isTrapezy():
    print("Фигура является равнобедренной трапецией")
else:
    print("Фигура не является равнобедренной трапецией")
print("ab = {}".format(trap.lengthSide(point_a, point_b)))
print("bc = {}".format(trap.lengthSide(point_b, point_c)))
print("cd = {}".format(trap.lengthSide(point_c, point_d)))
print("da = {}".format(trap.lengthSide(point_d, point_a)))
print("Периметр = {}, площадь = {}".format(trap.perimetr(), trap.square()))
