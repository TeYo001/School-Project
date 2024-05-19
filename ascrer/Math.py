import math

class Vec2:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vec2(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vec2(new_x, new_y)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Vec2(new_x, new_y)
    
    def screen_space_vec(self):
        return Vec2(self.x * (1/2), self.y)

    def world_space_vec(self):
        return Vec2(self.x * 2, self.y)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    #####
    #####
    #####
