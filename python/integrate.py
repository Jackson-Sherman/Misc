import numpy as np
import math
import matplotlib.pyplot as plt

def integrate(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area

theta = math.pi * 2 / 3

def fun2 (r,t,d): return (d*d + r*r*(1-math.sin(theta*(1-t)))) ** 0.5

def fun1 (r,t): return integrate(lambda d: fun2(r,t,d), 0, 1, 1000)

def fun0 (r): return integrate(lambda t: fun1(r,t), 0, 1, 1000)

count = 100

xs = [i/count for i in range(count+1)]

ys = [fun0(x) for x in xs]

plt.plot(xs,ys)