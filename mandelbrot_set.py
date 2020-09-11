from graphics import *
import math
import random

itMax = 1024

desiredSize = [256, 256]

win = GraphWin("Mandelbrot Set", desiredSize[0], 2 * int((1 + desiredSize[1]) / 2))

center = [-.743643135, .131825963]

#plus or minus. the 
pom = .000014628/2/2

portal = [[center[0] - pom, center[0] + pom], [center[1] - pom, center[1] + pom]] #[[-2,0.5],[-1.0,1.0]]

def toCanvas(pt):
    pt.x =  win.getWidth() * (pt.x - portal[0][0]) / (portal[0][1] - portal[0][0])
    pt.y = win.getHeight() * (pt.y - portal[1][0]) / (portal[1][1] - portal[1][0])
    
    return pt

def fromCanvas(pt):
    pt.x = pt.x * (portal[0][1] - portal[0][0]) / win.getWidth()  + portal[0][0]
    pt.y = pt.y * (portal[1][1] - portal[1][0]) / win.getHeight() + portal[1][0]
    
    return pt

def itterate(x, y):
    x *= (portal[0][1] - portal[0][0]) / win.getWidth()
    x += portal[0][0]
    y *= (portal[1][1] - portal[1][0]) / win.getHeight()
    y += portal[1][0]

    z = 0j
    c = complex(x, y)

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
cuanto = 0
realitMax = itMax
values = []
for x in range(0, win.getWidth() - 1):
    values.append([])
    for y in range(0, win.getHeight() - 1):
        cuanto += 1
        out = itterate(x, y)
        values[x].append(out)
        if out < theMin:
            theMin = out
            txt = "{} Min = point = ({}, {})   out = {}"
            print(txt.format(cuanto, x, y, out))
        
        if out > theMax:
            theMax = out
            txt = "{} Max = point = ({}, {})   out = {}"
            print(txt.format(cuanto, x, y, out))

print("click win to continue")
win.getMouse()

def scaling(val):
    outp = 0 if val <= theMin else math.log2(1 + val - theMin) / math.log2(1 + theMax - theMin)
    outp = 1 - outp
    return outp
    
xs = []
for x in range(0, win.getWidth() - 1):
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

def outToColor(its):
    output = scaling(its) #1 - math.log2(its[0]) / math.log2(its[1])
    if output == 0:
        return color_rgb(0, 0, 0)

    elif output < 0.25:
        output *= 4
        output = int(256 * output) #int(128 + 128 * output)
        return color_rgb(255, output, 0)

    elif output < 0.5:
        output *= 4
        output -= 1
        output = int(256 * output)
        return color_rgb(255, 255, output)

    else:
        output *= 2
        output -= 1
        output = int(255 - 255 * output)
        return color_rgb(output, output, 255)

def randomDots():
    while True:
        x = random.random() * win.getWidth()
        y = random.random() * win.getHeight()

        pt = Point(x,y)
        fromCanvas(pt)

        z = 0+0j
        c = complex(pt.x, pt.y)

        itteration = 0

        toCanvas(pt)
        pt.x = int(pt.x)
        pt.y = int(pt.y)

        while itteration < 2 ** 8 and abs(z) <= 2:
            z **= 2
            z += c

            itteration += 1
    
    
        circ = Circle(pt, 0)
        circ.setFill(color_rgb(itteration, 0, 0))
        #circ.setOutline(color_rgb(itteration, 0, 0))
        circ.setWidth(0)
        circ.draw(win)

def gradual():
    for tempx in range(0, win.getWidth() - 1):
        x = xs[tempx]
        if abs(portal[1][0]) == abs(portal[1][1]):
            halfHeight = int(win.getHeight() / 2)
            for y in range(0, halfHeight - 1):

                linea = Line(Point(x, y), Point(x, win.getHeight() - y))
                linea.setOutline(outToColor(itterate(x, y)))
                linea.setWidth(1)
                linea.draw(win)

            circ = Circle(Point(x, halfHeight), 0)
            circ.setFill(outToColor(itterate(x, halfHeight)))
            circ.setWidth(0)
            circ.draw(win)

        else:
            for y in range(1,win.getHeight() - 1):
                circ = Circle(Point(x, y), 1)
                circ.setFill(outToColor(values[x][y]))
                circ.setOutline(outToColor(values[x][y])) #itterate(x, y)))
                circ.setWidth(0)
                circ.draw(win)

    
gradual()
win.getMouse()
win.close()
