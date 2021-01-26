from . import hitboxes
from multipledispatch import dispatch
from math import sqrt


class CollisionDetector:
    @dispatch(type, hitboxes.Rect, hitboxes.Circle)
    def __new__(cls, rect: hitboxes.Rect, circle: hitboxes.Circle):
        for point in rect.outlines():
            if cls.distance(point, circle.center) <= circle.radius:
                return True
        return False

    @dispatch(type, hitboxes.Circle, hitboxes.Rect)
    def __new__(cls, circle: hitboxes.Circle, rect: hitboxes.Rect):
        return cls.__new__(rect, circle)

    @dispatch(type, hitboxes.Rect, hitboxes.Rect)
    def __new__(cls, rect1: hitboxes.Rect, rect2: hitboxes.Rect):
        for point in rect1.corners():
            if rect2.surrounds(point):
                return True
        for point in rect2.corners():
            if rect1.surrounds(point):
                return True
        return False

    @dispatch(type, hitboxes.Circle, hitboxes.Circle)
    def __new__(cls, circle1: hitboxes.Circle, circle2: hitboxes.Circle):
        return cls.distance(circle1.center, circle2.center) <= circle1.radius + circle2.radius

    @staticmethod
    def distance(p1: tuple[int, int], p2: tuple[int, int]):
        dx = p1[0] - p2[0]
        dy = p1[1] - p1[1]

        return sqrt(dx**2 + dy**2)
