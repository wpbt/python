# OOP in Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing the point!!! X={self.x}, Y={self.y}")

    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point(10, 20)
point.draw()
print(Point.zero())
print(point.zero())
