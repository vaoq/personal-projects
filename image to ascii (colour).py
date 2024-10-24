from PIL import Image
from PIL import ImageGrab


def get_pixels(
        image: Image, size: int
) -> list[int]:
    width, height = image.size
    aspect_ratio = height / width
    new_width = width // size
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((new_width, round(new_height)))
    return image.getdata()


def get_colors(
        image: Image, size: int
) -> list[int]:
    width, height = image.size
    aspect_ratio = height / width
    new_width = width // size
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((new_width, round(new_height)))
    return image.getdata()


def image_to_ascii_art(
    img_path: str, output_file: str, background_color_rgb: list[int], size: int
) -> str:

    # load images
    grayscale = Image.open(img_path).convert("L")
    rgb = Image.open(img_path).convert("RGB")

    # get array of pixel brightness and pixel colours
    pixels = get_pixels(grayscale, size)
    colors = get_colors(rgb, size)

    # get size for later
    image_width = rgb.size[0] // size

    # characters to use for the image
    chars = '@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:\'        '[::-5]
    chars = '@#XOhSje1{J?!^- '[::-1]
    #chars = '█▓░'
    #chars = '█'
    #chars = ' '

    if type(background_color_rgb) == list:
        bg = f'\x1b[48;2;{';'.join([str(background_color_rgb[i]) for i in range(3)])}m'
    else:
        bg = ''

    # assign each pixel to a character
    new_pixels = [chars[(int(pixel/(255//len(chars)+1)))] for pixel in pixels]

    text_output = ''.join(new_pixels)
    ascii_image = [
        text_output[index : index + image_width]
        for index in range(0, len(text_output), image_width)
    ]

    for i in range(len(new_pixels)):
        new_pixels[i] = f'\x1b[38;2;{colors[i][0]};{colors[i][1]};{colors[i][2]}m{new_pixels[i]}'
        if i % image_width == 0 and i!=0:
            print('\033[1;31;49m')
        print(bg+new_pixels[i], end=new_pixels[i])

    screenshot = ImageGrab.grab(all_screens=True)
    screenshot.save('ss.png', 'PNG')  # Equivalent to `screenshot.save(filepath, format='PNG')`


    ascii_image = "\n".join(ascii_image)

    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
        f.close()

    return ''

image_to_ascii_art("example6.png",
                   'x',
                   [0,0,0],
                   5)
