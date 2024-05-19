from enum import Enum
from copy import copy
from math import sqrt

class Pixel:
    def __init__(self, shade:float=0.0, custom=None):
        self.shade = float(shade)
        self.custom = custom # must be eighter None or a char

class Pallet:
    def __init__(self, chars: list, distribute):
        self.chars = chars
        # a function that takes a value from 0 to 1 and returns a char from chars based on that value
        self.distribute = distribute

def linear_distribution(shade:float, chars:list):
    return chars[int(shade * (len(chars) - 1))]

def dark_exponential_distribution(shade:float, chars:list):
    return chars[int(sqrt(sqrt(shade)) * (len(chars) - 1))]

class Screen:
    def __init__(self, size, default_pixel:Pixel=Pixel(shade=0.0)):
        self.width = size[0]
        self.height = size[1]
        self.default_pixel = default_pixel
        self.pixels = [None] * (self.width * self.height)
        self.clear()
    
    def clear(self):
        for i in range(self.width * self.height):
            self.pixels[i] = copy(self.default_pixel)

def render_pixel(pixel: Pixel, pallet: Pallet) -> str:
    if pixel.custom is not None:
        return pixel.custom
    return pallet.distribute(pixel.shade, pallet.chars)

def render_screen(screen: Screen, pallet: Pallet) -> str:
    ret_str = ""
    for y in range(screen.height):
        for x in range(screen.width):
            ret_str += render_pixel(
                    screen.pixels[y * screen.width + x],
                    pallet)
        ret_str += "\n"
    return ret_str

# fragment = func (x, y) -> Pixel
def call_fragment(screen: Screen, fragment):
    for y in range(screen.height):
        for x in range(screen.width):
            new_pixel = fragment(x, y)
            if new_pixel is not None:
                screen.pixels[y * screen.width + x] = new_pixel


