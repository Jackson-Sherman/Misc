from PIL import Image
import blurs
import math



def draw():
    im = Image.new("RGB", (128, 128), "black")
    pixels = im.load()

    def fun(X,Y):
        centeredOn = (0.5, 0.5)
        radius = (0.5, 0.5)
        
        x = radius[0] * (X / im.size[0] * 2 - 1) + centeredOn[0]
        y = radius[1] * (Y / im.size[1] * 2 - 1) + centeredOn[1]
        
        out = int(256 * ((x + y) % 1))
        output = (out, out, out)
        return output

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pixels[x, y] = fun(x, y)

    return im



img = draw()
img.show()

newboi = blurs.errorDiff(img)
newboi.show()



