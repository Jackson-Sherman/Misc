from PIL import Image
import random
import math
from hsv import hsv_to_rgb


print("Pick the number of the color you want:")
cual = int(input("0=random, 1=palette, 2=hue random? "))
strings = ["750787", "004dff", "008026", "ffed00", "ff8c00", "e40303"]
palette = []
for x in range(len(strings)):
    #stri = "#" + strings[x]
    lista = []

    for i in (0,1,2):
        lista.append(int(strings[x][i * 2:i * 2 + 2], 16))
    
    palette.append(tuple(lista))
    #stri += ": {}".format(palette[len(palette) - 1])

    #print(stri)

img = Image.new("RGB", (250,250), "black")

px = img.load()

def color_choice(which, X, Y):
    def rand():
        def scaled():
            
            return int(math.floor(256 * random.random()))
        
        return (scaled(), scaled(), scaled())

    def from_palette():

        return palette[int(math.floor(len(palette) * random.random()))]

    def from_hsv():

        return hsv_to_rgb(random.random(), random.random(), random.random())

    output = ()

    if cual == 0:
        output = rand()

    elif cual == 1:
        output = from_palette()

    else:
        output = from_hsv()

    return output


for x in range(img.size[0]):
    for y in range(img.size[1]):
        px[x, y] = color_choice(cual, x, y)

img.save("canvas_profile_pic.png")
img.show()