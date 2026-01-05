from collections.abc import Generator
import numpy as np
from PIL import Image

modulus = 2**32-1
a, c, seed = 2, 3, 4

# LCG
values = []
for i in range(1024**2):
    seed = (a * seed + c) % modulus
    values.append(seed)

data = np.zeros( (1024,1024,3), dtype=np.uint8 )
index = 0

for row in range(len(data)):
    for column in range(len(data[row])):
        colour = int((values[index] / modulus) * 255)
        data[row][column] = [colour]
        index += 1

print(values[0:10])

image = Image.fromarray(data)
image.show()