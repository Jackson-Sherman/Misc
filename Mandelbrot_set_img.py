from PIL import Image
import math
import random

itMax = 2 ** 12

desiredSize = [int(2560/10), int(1600/10)]
spots = {#                               .131825963
    "coolspot": {"center": [-.743643135, .1318263], "pom": [.000014628/2*0.85, .000014628/2/2560*1600*0.85]},
    "mainspot": {"center": [-.75, 0], "pom": [1.5, 1.5]}
}

center = spots["coolspot"]["center"]
#plus or minus. the canvas radius, if you will
pom = spots["coolspot"]["pom"]

        


img = Image.new("RGB", (desiredSize[0], desiredSize[1]), "black")
px = img.load()



portal = [[center[0] - pom[0], center[0] + pom[0]], [center[1] - pom[1], center[1] + pom[1]]] #[[-2,0.5],[-1.0,1.0]]

def toCanvas(pt):
    pt.x = desiredSize[0] * (pt.x - portal[0][0]) / (portal[0][1] - portal[0][0])
    pt.y = desiredSize[1] * (pt.y - portal[1][0]) / (portal[1][1] - portal[1][0])
    
    return pt

def fromCanvas(pt):
    pt.x = pt.x * (portal[0][1] - portal[0][0]) / desiredSize[0] + portal[0][0]
    pt.y = pt.y * (portal[1][1] - portal[1][0]) / desiredSize[1] + portal[1][0]
    
    return pt

def itterate(x, y):
    #x *= (portal[0][1] - portal[0][0]) / desiredSize[0]
    #x += portal[0][0]
    #y *= (portal[1][1] - portal[1][0]) / desiredSize[1]
    #y += portal[1][0]

    z = 0j
    c = complex(x * (portal[0][1] - portal[0][0]) / desiredSize[0] + portal[0][0], y * (portal[1][1] - portal[1][0]) / desiredSize[1] + portal[1][0])

    itteration = 0

    while itteration < itMax and abs(z) <= 2:
        z **= 2
        z  += c
    
        itteration += 1
    
    #output = itteration / itMax
    return itteration
    #output = 1 - math.log2(itteration) / math.log2(itMax)

theMin = itMax + 1
theMax = 0 - 1
realitMax = itMax
values = []

for x in range(0, desiredSize[0]):
    values.append([])
    for y in range(0, desiredSize[1]):
        out = itterate(x, y)
        values[x].append(out)
        if out < theMin:
            theMin = out
        
        if out > theMax:
            theMax = out

    print("{}".format(100 * x / desiredSize[0]))

def scaling(its):

    def linScale(val):
        outp = 1 - (1 + val - theMin) / (1 + theMax - theMin)
        return outp

    def logScale(val):
        outp = 0 if val <= 0 else math.log2(2 + val - theMin) / math.log2(2 + theMax - theMin)
        outp = 1 - outp
        return outp

    return logScale(its)
    
xs = []
for x in range(0, desiredSize[0]):
    xs.append(x)


def scramble(list):
    randomList = []
    for i in range(0, len(list)):
        randomList.append(random.random())
    
    for a in range(0, len(list) - 1):
        for b in range(a + 1, len(list)):
            if randomList[a] < randomList[b]:
                tempB = list[b]
                list[b] = list[a]
                list[a] = tempB

                tempA = randomList[a]
                randomList[a] = randomList[b]
                randomList[b] = tempA

scramble(xs)

def outToColor(its, loops):
    esto = scaling(its)
    esto *= loops
    esto %= 1

    def greyscale(ok):
        outtuple = (0, 0, 0)
        if 0 < ok:
            outnum = 255 - int(ok * 256)
            outtuple = (outnum, outnum, outnum)
        return outtuple

    def bluetoorange(output):
        if output == 0:
            return (0, 0, 0)

        elif output < 0.25:
            output *= 4
            output = int(256 * output) #int(128 + 128 * output)
            return (255, output, 0)

        elif output < 0.5:
            output *= 4
            output -= 1
            output = int(256 * output)
            return (255, 255, output)

        else:
            output *= 2
            output -= 1
            output = int(255 - 255 * output)
            return (output, output, 255)

    def hue(ok):
        ok *= 6

        if ok <= 0:
            ok = abs(ok)
            ok %= 1
            return (0, 0, 0)
            
        elif ok < 1:
            ok %= 1
            ok *= 256
            ok = int(ok)
            return (255, ok, 0)
            
        elif ok < 2:
            ok %= 1
            ok *= 256
            ok = int(ok)
            ok *= -1
            ok += 255
            return (ok, 255, 0)
            
        elif ok < 3:
            ok %= 1
            ok *= 256
            ok = int(ok)
            return (0, 255, ok)
            
        elif ok < 4:
            ok %= 1
            ok *= 256
            ok = int(ok)
            ok *= -1
            ok += 255
            return (0, ok, 255)

        elif ok < 5:
            ok %= 1
            ok *= 256
            ok = int(ok)
            return (ok, 0, 255)
            
        else:
            ok %= 1
            ok *= 256
            ok = int(ok)
            ok *= -1
            ok += 255
            return (255, 0, ok)

    def specialHue(ok):
        ok *= 6

        if ok <= 0:
            ok = abs(ok)
            ok %= 1
            return (0, 0, 0)
            
        elif ok < 1:
            ok %= 1
            ok *= 256
            ok = int(ok)
            return (128 + int(ok / 2), ok, 0)
            
        elif ok < 2:
            ok %= 1
            ok *= 256
            ok = int(ok)
            return (255, 255, ok)
            
        elif ok < 3:
            ok %= 1
            ok *= 256
            ok = int(ok)
            ok *= -1
            ok += 255
            return (ok, 255, 255)
            
        elif ok < 4:
            ok %= 1
            ok *= 256
            ok = int(ok)
            ok *= -1
            ok += 255
            return (0, ok, 255)

        elif ok < 5:
            ok %= 1
            ok *= 128
            ok = int(ok)
            return (ok, 0, 255 - ok)
            
        else:
            ok %= 1
            ok *= 128
            ok = int(ok)
            ok *= -1
            ok += 127
            return (127, 0, ok)
    
    return specialHue(esto)
            

def gradual():
    for tempx in range(0, desiredSize[0]):
        x = xs[tempx]
        for y in range(desiredSize[1] - 1, -1, -1):
            color = outToColor(values[x][y], 4)
            px[x,desiredSize[1] - 1 - y] = color
        
        print("{}".format(100 * tempx / desiredSize[0]))

    
gradual()

img.save("mandystuff.png")
img.show()
