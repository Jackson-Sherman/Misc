import re

def int_list(string, seperator = ","):
    temp = re.split(seperator, string)
    for i, j in enumerate(temp):
        temp[i] = int(j)
    return temp
still_going = True
size = int_list(input("Dimensions of the circle: "))

def dentro(tup):
    return lambda x, y: bool(((2 * x - tup[0])/(1 - tup[0])) ** 2 + ((2 * y - tup[1])/(1 - tup[1])) ** 2 < 1)

while still_going:
    inside = dentro(size)
    pnt = int_list(input("point to test as a tuple: "))
    print(inside(pnt[0], pnt[1]))

    size = int_list(input("If you want to draw another circle, enter the dimensions, otherwise just press \"enter\" "))
    if not(size):
        still_going = False