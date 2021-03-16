from PIL import Image

imgStr = '/Users/jacksonsherman/Downloads/montero.png'# input("filepath to the png: ")

width  = 8 # int(input("tile horizontally: "))
height = 5 # int(input("  tile vertically: "))

screen_size = 2560, 1600

scale = min(screen_size[0] // width, screen_size[1] // height)

start = Image.open(imgStr)

size = start.getbbox()[2:]

resized = start.resize((scale,scale))

img = Image.new('RGBA',screen_size)

for i in range(height):
    for j in range(width):
        img.paste(resized, (j * scale, i * scale))

img.show()