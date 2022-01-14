import math


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f'Площадь прямоугольника  {self.get_area()}'

"BONUS, Скучно, два раза подряд, площадь прямоугольника считать!"
"Вычисление площади треугольника по формуле Герона"

class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.sumside = (a + b + c) / 2
    def get_area(self):
        return round(math.sqrt(self.sumside * (self.sumside - self.side_a) * (self.sumside - self.side_b) * (self.sumside - self.side_c)), 2)
    def __str__(self):
        return f'Площадь треугольника {self.get_area()}'

rectangle = Rectangle(7, 9)
triangle = Triangle(11, 13, 15)

print(rectangle)
print(triangle)
