from itertools import product


class Rect:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def outlines(self):
        return [(self.x, y) for y in range(self.y, self.y + self.height + 1)] + \
               [(self.x + self.width, y) for y in range(self.y, self.y + self.height + 1)] + \
               [(x, self.y) for x in range(self.x, self.x + self.width + 1)] + \
               [(x, self.y + self.height) for x in range(self.x, self.x + self.width + 1)]

    def corners(self):
        return list(product((self.x, self.x + self.width), (self.y, self.y + self.height)))

    def surrounds(self, point: tuple[int, int]):
        return self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height


class Circle:
    def __init__(self, x_center: int, y_center: int, radius: int):
        self.x = x_center
        self.y = y_center
        self.radius = radius

    @property
    def center(self):
        return self.x, self.y
