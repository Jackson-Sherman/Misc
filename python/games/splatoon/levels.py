import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import re
next_level = [
    None,
    10,
    28,
    46,
    65,
    85,
    105,
    126,
    148,
    170,
    193,
    216,
    241,
    266,
    291,
    318,
    346,
    374,
    403,
    433,
    450,
    465,
    480,
    495,
    510,
    525,
    540,
    555,
    570,
    585,
    620,
    655,
    690,
    725,
    760,
    790,
    820,
    850,
    880,
    900,
    920,
    940,
    950,
    960,
    970,
    980,
    985,
    990,
    995,
    1000,
]
current_level = 10
current_xp = 0
accumulated_xp = [None, 0]
for i in range(2,len(next_level)+1):
    accumulated_xp += [accumulated_xp[i-1] + next_level[i-1]]

def points(string):
    def amount(char):
        if char == "l":
            return 8
        elif char == "w":
            return 14

    def recur(thread):
        if thread == "":
            return 0
        else:
            return amount(thread[0]) + recur(thread[1:])

    return recur(string)
d = {

}
current = "l"
i = 1
goal = next_level[current_level] - current_xp
while 8*i < goal:
    d["l"*i] = (8*i, i)
    i += 1
d["l"*i] = (8*i, i)
current = "l"*i

while points(current) < goal or current != "w" * len(current):
    if points(current) >= goal:
        while current[:-1] + "w" in d:
            current = current[:-1]
        current = current[:-1] + "w"
        d[current] = points(current)
        



def func(x,a,b,c):
    return (a*x + b)*x + c

x = np.arange(2, len(accumulated_xp), 1)
y = np.array(accumulated_xp[2:])
# x = np.arange(1, len(next_level), 1)
# y = np.array(next_level[1:])
popt, pcov = curve_fit(func, x, y)
plt.plot(x, y, "b-")
z = func(x, *popt)
plt.plot(x, z, "g--")

y_mean = sum([each for each in y])/len(y)
sstot = sum([(each - y_mean) ** 2 for each in y])
ssres = sum([(y[i] - z[i]) ** 2 for i in range(len(x))])

r_squared = 1 - ssres / sstot

print(r_squared)

plt.show()
