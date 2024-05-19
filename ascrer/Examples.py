import imageio.v3 as iio
from Screen import *
import os
from Pallets import *
from Shapes import *
from Fragments import *
import time

def clear_terminal():
    if os.name == "nt": # on windows
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("operating system not supported")
        exit(1)

def draw_image_pixel(x, y, image):
    color_top = image[y * 4][x * 2]
    color_bottom = image[y * 4 + 1][x * 2]
    color = (color_top + color_bottom)
    shade = max(color[0], color[1], color[2]) / 255
    return Pixel(shade)

def draw_image(image):
    return lambda x, y: draw_image_pixel(x, y, image)

def image_to_ascii(image_path: str, pallet: Pallet): 
    image = None
    try:
        image = iio.imread(image_path)
    except:
        print("Could not read image.")
        return None
    screen = Screen((int(image.shape[1] / 2.0), int(image.shape[0] / 4.0)))
    call_fragment(screen, draw_image(image))
    print(render_screen(screen, LARGE_PALLET))

def select_file():
    while True:
        file_path = input("input complete file path for .jpg image or [1: homer, 2: mona lisa]: ")
        match file_path:
            case "1":
                return "test.jpg"
            case "2":
                return "Mona Lisa.jpg"
        if len(file_path) == 0:
            print("must input a valid file path or example number")
            continue
        if file_path[len(file_path)-len(".jpg"):len(file_path)] != ".jpg":
            print("must be a .jpg file")
            continue
        return file_path

def select_pallet():
    pallet = None
    while True:
        pallet_select_str = input(f"1: \"{LARGE_PALLET.chars}\"\n2: \"{STANDARD_PALLET.chars}\"\n3: \"{SIMPLE_PALLET.chars}\"\nselect_pallet: ")
        
        match pallet_select_str:
            case "1":
                pallet = LARGE_PALLET
            case "2":
                pallet = STANDARD_PALLET
            case "3":
                pallet = SIMPLE_PALLET
        if pallet == None:
            print("invalid pallet option, select between [1, 2, 3]")
            continue
        else:
            return pallet

def picture_example():
    while True:
        clear_terminal()
        file_path = select_file()
        pallet = select_pallet()
        if pallet is None:
            continue
        if image_to_ascii(file_path, pallet) is None:
            input() # wait for key input before quiting
            continue
        else:
            break

def box_example():
    clear_terminal()
    sign = 1
    i = 1
    while True:
        screen = Screen((100, 100))
        box = Rect(Vec2(50, 50), abs(2 * i), abs(2 * i))
        clear_terminal()
        call_fragment(screen, draw_rect(box))
        print(render_screen(screen, LARGE_PALLET))
        time.sleep(0.2)
        i += sign
        if i >= 10 or i <= -10:
            sign = -sign


def circle_example():
    clear_terminal()
    velocity = 0
    gravity = 1
    y_pos = 50
    bounces = 0
    squish_amount = 5
    while True:
        screen = Screen((100, 100))
        circle = Circle(Vec2(50, y_pos), 10)
        clear_terminal()
        call_fragment(screen, draw_circle(circle))
        print(render_screen(screen, LARGE_PALLET))
        time.sleep(0.1)
        y_pos += velocity
        velocity += gravity
        if y_pos >= 100 - circle.radius + squish_amount:
            velocity = -velocity * 0.5
            y_pos = 100 - circle.radius - 1 + squish_amount
            bounces += 1
            if bounces == 10:
                velocity = -10
                bounces = 0

def play_example():
    clear_terminal()
    while True:
        example_str = input("1: picture example\n2: box example\n3: circle_example\nselect example: ")
        match example_str:
            case "1":
                picture_example()
            case "2":
                box_example()
            case "3":
                circle_example()
        print("invalid example number given")

if __name__ == "__main__":
    play_example()
        
