from Shapes import *
from Screen import *
from scipy.stats import norm
from scipy.special import expit
from math import sqrt

def draw_circle_pixel(x, y, circle):
    screen_pos = Vec2(x, y).screen_space_vec()
    dist = screen_pos.distance(circle.pos)
    if dist <= circle.radius:
        return Pixel(1)
    else:
        return None

def draw_circle(circle: Circle):
    return lambda x, y: draw_circle_pixel(x, y, circle)

# the border goes from 0 -> 1
def draw_circle_smooth_pixel(x, y, circle, border):
    screen_pos = Vec2(x, y).screen_space_vec()
    dist = screen_pos.distance(circle.pos)
    if dist <= circle.radius * border:
        return Pixel(1)
    elif dist <= circle.radius:
        shade = dist / circle.radius # 0.8 -> 1
        shade = (shade - border) * (1 / (1 - border))
        shade = 1 - shade ** 2 * sqrt(shade)
        return Pixel(shade)
    else:
        return None

def draw_circle_smooth(circle: Circle, border=0.2):
    return lambda x, y: draw_circle_smooth_pixel(x, y, circle, 1 - border)

def draw_line_pixel(x, y, line: Line):
    screen_pos = Vec2(x, y).screen_space_vec()
    dist = (line.end.x - line.start.x) * (screen_pos.y - line.start.y) - (screen_pos.x - line.start.x) * (line.end.y - line.start.y)
    dist = abs(dist)
    dist /= sqrt((line.end.x - line.start.x) ** 2 + (line.end.y - line.start.y) ** 2)
    if dist <= line.thickness:
        return Pixel(1)
    else:
        return None

def draw_rect_pixel(x, y, rect):
    screen_pos = Vec2(x, y).screen_space_vec()
    x_left_limit = rect.pos.x - rect.width / 2
    x_right_limit = rect.pos.x + rect.width / 2
    y_top_limit = rect.pos.y + rect.height / 2
    y_bottom_limit = rect.pos.y - rect.height / 2

    inside_rect = screen_pos.x >= x_left_limit and screen_pos.x <= x_right_limit
    inside_rect = inside_rect and screen_pos.y <= y_top_limit and screen_pos.y >= y_bottom_limit
    if inside_rect:
        return Pixel(1)
    else:
        return None

def draw_rect(rect: Rect):
    return lambda x, y: draw_rect_pixel(x, y, rect)

def draw_line(line: Line):
    return lambda x, y: draw_line_pixel(x, y, line)


    
    
    
