import unittest
from setton.Pygame.collisions import *
from setton.Pygame.hitboxes import *


class CollisionsTester(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rect1 = Rect(100, 100, 50, 50)
        cls.rect2 = Rect(120, 130, 100, 100)
        cls.circle1 = Circle(150, 150, 15)
        cls.circle2 = Circle(100, 200, 30)

    def test_rect_rect(self):
        self.assertTrue(CollisionDetector(self.rect1, self.rect2))

    def test_rect_circle(self):
        self.assertTrue(CollisionDetector(self.rect1, self.circle1))

    def test_circle_rect(self):
        self.assertTrue(CollisionDetector(self.circle1, self.rect2))

    def test_circle_circle(self):
        self.assertFalse(CollisionDetector(self.circle1, self.circle2))


if __name__ == '__main__':
    unittest.main()