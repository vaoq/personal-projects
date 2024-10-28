from PIL import Image
from PIL import ImageGrab # for the future <3


def get_image(
        image: Image, size: int
) -> list[int]:
    width, height = image.size
    aspect_ratio = height / width
    new_width = width // size
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((new_width, round(new_height)))
    return image.getdata()


def image_to_ascii_art(
    img_path: str, background_color_rgb: list[int] | None, size: int, char_preset: str
) -> str:

    # load grayscale and rgb version of image
    grayscale = Image.open(img_path).convert("L")
    rgb = Image.open(img_path).convert("RGB")

    # get arrays of pixel brightness and pixel colour
    pixels = get_image(grayscale, size)
    colors = get_image(rgb, size)

    # get width for usage later
    image_width = rgb.size[0] // size

    # characters to use for the conversion
    chars = ['@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:\'        ', '@#XOhSje1{J?!^- ', '█▓░', '█', ' '][abs(int(char_preset))][::-1 if char_preset[0] == '-' else 1]

    # if bg is a list assign colour ansi code, else assign to nothing
    bg = (f'\x1b[48;2;{';'.join([str(background_color_rgb[i])for i in range(3)])}m'if isinstance(background_color_rgb, list)else'')

    # assign each pixel to a character
    new_pixels = [chars[(int(pixel/(255//len(chars)+1)))] for pixel in pixels]

    ascii_image = ''
    for i in range(0, len(new_pixels)):
        ascii_image += ('\033[1;31;49m\n' if i % image_width == 0 and i!=0 else '') + bg + f'\x1b[38;2;{colors[i][0]};{colors[i][1]};{colors[i][2]}m{new_pixels[i]}'*2

    return ascii_image + '\033[1;31;49m'

print(image_to_ascii_art("images\\example6.png",     # Directory Path of image to convert
                   [0,0,0],      # RGB Value of background (Hint: Typically looks better with black background)
                   10,                    # Size of image (Hint: Higher value = Lower Resolution)
                   '-3'))          # Which set of characters to use in the 'chars' array. Use negative to reverse which chars are used for bright/dark areas.
