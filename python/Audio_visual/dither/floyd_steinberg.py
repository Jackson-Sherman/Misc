from PIL import Image
import numpy as np

def realign(inp):
    def doing(num):
        if inp <= 0:
            return 0
        elif inp < 256:
            return int(inp)
        else:
            return 255
    
    if isinstance(inp, np.ndarray):
        out = np.empty([len(inp), len(inp[0])])
        for y in range(len(inp)):
            for x in range(len(inp[y])):
                out[y][x] = doing(inp[y][x])
        return out


infile = Image.open("/Users/jacksonsherman/Downloads/reputation.png")
size = infile.getbbox()[2:]
px = infile.load()
print(size)
array = np.empty([size[0],size[1]])
print(type(array))
for y in range(size[0]):
    for x in range(size[1]):
        array[y][x] = px[x, y] / 255

copy = Image.fromarray(realign(array))
copy.show()