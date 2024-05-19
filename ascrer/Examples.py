import imageio.v3 as iio
from Screen import *
import os
from Pallets import *

def clear_terminal():
    if os.name == "nt": # on windows
        system("cls")
    elif os.name == "posix":
        system("clear")
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

def image_to_ascii(image_path: str): 
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
        file_path = input("input complete file path for .jpg image")
        if len(file_path) == 0:
            print("must input a valid file path")
            continue
        if file_path[len(file_path)-len(".jpg"):len(file_path)] != ".jpg":
            print("must be a .jpg file")
            continue
        return file_path

def select_pallet():
    while True:
        pallet_select_str = input(f"1: \"{LARGE_PALLET.chars}\"\n2: \"{STANDARD_PALLET.chars}\"\n3: \"{SIMPLE_PALLET.chars}\"\nselect_pallet:")
        pallet = None
        match pallet_select_str:
            case "1":
                pallet = LARGE_PALLET
            case "2":
                pallet = STANDARD_PALLET
            case "3":
                pallet = SIMPLE_PALLET
        return pallet

def picture_example():
    while True:
        clear_terminal()
        file_path = select_file()
        pallet = select_pallet()
        if pallet is None:
            continue
        if image_to_ascii(file_path) is None:
            continue
        break
        
