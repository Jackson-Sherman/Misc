from PIL import Image, ImageDraw
import math

images = []
size = (400,400)
unit = min(size) * 1/8
def project(coo):
    coo = [coo[i] * unit for i in range(len(coo))]
    fov = size[0] * 0.8
    scaled = fov / (fov + coo[2])
    return [coo[0] * scaled + size[0] / 2, coo[1] * scaled + size[1] / 2, scaled]


def quick(lst):
    if len(lst) <= 1:
        return lst
    else:
        check = lst[0]["depth"]
        before = []
        after = []
        for i in range(1,len(lst)):
            if lst[i]["depth"] >= check:
                before += [lst[i]]
            else:
                after += [lst[i]]
        return quick(before) + [check] + quick(after)

a = 0
while a < math.pi * 2:
    im = Image.new("RGB", size, (255,255,255))
    draw = ImageDraw.Draw(im)
    items = []
    for Z in range(-4, 4):
        for X in range(-4, 4):
            for Y in range(-4, 4):
                x = X + 0.5 + math.cos(a)
                y = Y + 0.5
                z = Z + 0.5 + math.sin(a)
                pnt = project([x, y, z])
                rad = int(2 * pnt[2] + 0.5)
                items.append({
                    "loc":(pnt[0]-rad, pnt[1]-rad, pnt[0]+rad, pnt[1]+rad),
                    "fill":(127*(X%2),127*(Y%2),127*(Z%2)),
                    "depth": Z
                })
    quick(items)
    for cosa in items:
        draw.ellipse(cosa["loc"], fill=cosa["fill"])
    images.append(im)
    a += math.pi / 180



images[0].save("dagif.gif", save_all=True, append_images=images[1:], optimize=False, duration=20, loop=0)
