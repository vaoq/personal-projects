from PIL import Image;from PIL import ImageGrab
def get_pixels(image: Image, size: int) -> list[int]:width, height = image.size;aspect_ratio = height / width;new_width = width // size;new_height = aspect_ratio * new_width * 0.55;image = image.resize((new_width, round(new_height)));return image.getdata()
def get_colors(image: Image, size: int) -> list[int]:width, height = image.size;aspect_ratio = height / width;new_width = width // size;new_height = aspect_ratio * new_width * 0.55;image = image.resize((new_width, round(new_height)));return image.getdata()
def image_to_ascii_art(img_path: str, background_color_rgb: list[int] | None, size: int, char_preset: str) -> str:
    grayscale =Image.open(img_path).convert("L");rgb = Image.open(img_path).convert("RGB");pixels = get_pixels(grayscale, size);colors = get_colors(rgb, size);image_width = rgb.size[0] // size;chars = ['@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:\'        ','@#XOhSje1{J?!^- ','█▓░','█',' '][abs(int(char_preset))][::-1 if char_preset[0] == '-' else 1];bg = (f'\x1b[48;2;{';'.join([str(background_color_rgb[i])for i in range(3)])}m'if isinstance(background_color_rgb, list)else'');new_pixels = [chars[(int(pixel/(255//len(chars)+1)))] for pixel in pixels]
    for i in range(len(new_pixels)):
        new_pixels[i] = f'\x1b[38;2;{colors[i][0]};{colors[i][1]};{colors[i][2]}m{new_pixels[i]}'
        if i % image_width == 0 and i!=0:print('\033[1;31;49m');print(bg+new_pixels[i], end=new_pixels[i])
    screenshot = ImageGrab.grab(all_screens=True);screenshot.save('ss.png', 'PNG');return ''
    image_to_ascii_art("example3.jpg",[0,0,0],30,'-3')