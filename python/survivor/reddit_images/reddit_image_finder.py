from PIL import Image
import requests
from io import BytesIO
import urllib.request
import re

url = "http://b.thumbs.redditmedia.com/vf9DyMv9gsuCHOMIyZyxaoaFzOcBcJu2ghqNm9nq_9g.css"

fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = str(mybytes.decode("utf8"))
fp.close()

splitAtQuotes = mystr.split('"')

pngurls = set()

for each in splitAtQuotes:
    if 4 < len(each) and each[-4:] == '.png':
        if each[:2] == '//':
            each = 'http:' + each
        
        pngurls |= {each}

pngurls = list(pngurls)
pngurls.sort()
images = ()


for each in pngurls:
    print(each, end=" ")
    images += (Image.open(BytesIO(requests.get(each).content)),)
    print(images[-1].size)
    if images[-1].size != (300, 300):
        pass

images = tuple([img for img in images if img.size == (300, 300)])

s = images[0].size

squareSide = len(images) ** 0.5
squareSide = squareSide if squareSide % 1 == 0 else int(squareSide) + 1

output = Image.new("RGB", (s[0] * squareSide, s[1] * squareSide))

for i in range(len(images)):
    x = i % squareSide
    y = i // squareSide
    x *= s[0]
    y *= s[1]
    output.paste(images[i], (x,y))
    print(("{:>" + str(len(str(len(images) + 1))) + "} / ").format(i + 1) + str(len(images)))

output.save("/Users/jacksonsherman/Desktop/Code/git/Personal/Misc/python/survivor/reddit_images/collage.png")
output.show()