from PIL import Image
from random import random
skin = Image.new("RGBA", (64, 64), (0,0,0,0))

px = skin.load()

def rand():
    return int(256 * random())


for x in range(skin.size[0]):
    for y in range(skin.size[1]):
        if (32 <= x and y < 16) or (32 <= y):
            if random() < 0.5:
                px[x, y] = (0, 0, 0, 0)
            else:
                px[x, y] = (0, 0, 0, 255)
            if 48 <= y and 16 <= x and x < 48:
                px[x, y] = (rand(), rand(), rand(), 255)
        else:
            px[x, y] = (rand(), rand(), rand(), 255)

skin.save("skin?.png")
skin.show()