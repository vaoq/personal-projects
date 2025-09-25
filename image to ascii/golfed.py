from PIL import Image
def get_image(image: Image, size: int) -> list[int]:
    width, height = image.size;aspect_ratio = height / width;new_width = width // size;new_height = aspect_ratio * new_width * 0.55;image = image.resize((new_width, round(new_height)));return image.getdata()
def image_to_ascii_art(ip, bcrgb, s: int, c: str):
    i = Image.open(ip);grayscale = i.convert("L");rgb = i.convert("RGB");p = get_image(grayscale, s);o = get_image(rgb, s);w=rgb.size[0]//s;chars = ['@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:\'        ', '@#XOhSje1{J?!^- ', '█▓░', '█', ' '][abs(int(c))][::-1 if c[0] == '-' else 1];bg = (f'\x1b[48;2;{';'.join([str(bcrgb[i]) for i in range(3)])}m'if isinstance(bcrgb, list)else '');new_pixels = [chars[(int(pixel/(255//len(chars)+1)))] for pixel in p];ascii_image = ''
    for i in range(0, len(new_pixels)):ascii_image += ('\033[1;31;49m\n' if i % w == 0 and i!=0 else '') + bg + f'\x1b[38;2;{o[i][0]};{o[i][1]};{o[i][2]}m{new_pixels[i]}'*2
    return ascii_image + '\033[1;31;49m'
print(image_to_ascii_art("images\\example6.png",[0,0,0],10,'-3'))