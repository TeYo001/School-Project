from Math import *

class Circle:
    def __init__(self, pos: Vec2, radius):
        self.pos = pos.screen_space_vec()
        self.radius = float(radius)

class Rect:
    def __init__(self, pos: Vec2, width, height):
        self.pos = pos.screen_space_vec()
        self.width = float(width)
        self.height = float(height)

    def top_left(self):
        return Vec2(self.pos.x - self.width / 2, self.pos.y - self.height / 2)

    def bottom_right(self):
        return Vec2(self.pos.x + self.width / 2, self.pos.y + self.height / 2)

class Line:
    def __init__(self, start: Vec2, end: Vec2, thickness):
        self.start = start
        self.end = end
        self.thickness = float(thickness)
