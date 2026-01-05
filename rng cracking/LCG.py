import numpy as np
from PIL import Image

# Initialise values for generator
modulus = 2**32-1
a, c, seed = 2, 3, 4
size = 1024

# LCG Generator
values = []

for i in range(size**2):
    seed = (a * seed + c) % modulus
    values.append(seed)

# Generate Image
index = 0
data = np.zeros((size, size, 3), dtype=np.uint8)

for row in range(len(data)):
    for column in range(len(data[row])):
        colour = int((values[index] / modulus) * 255)
        data[row][column] = [colour]
        index += 1

image = Image.fromarray(data)
image.show()

print(values[0:10]) if 1 == 1 else ()

