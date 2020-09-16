import turtle
import random

pen = turtle.Turtle()
pen.speed(15)
pen.penup()

def hexa(num):
    string = hex(num)[2:]
    string = string.lower()
    while len(string) > 2:
        string = string[1:]
    while len(string) < 2:
        string = "0" + string
    return string

for i in range(99999999):
    x = int(random.random() * 256)
    y = int(random.random() * 256)
    pen.goto(x,y)
    pen.pendown()
    pen.color("#" + hexa(int(random.random() * 256))+ hexa(x)+ hexa(y))
    pen.dot()
    pen.penup()

