import numpy as np  
import matplotlib.pyplot as plt  

x = np.arange(0, 5, 0.1)  
y = np.sin(x)  
plt.plot(x, y)  

import matplotlib.pyplot as plt
import numpy as np


class line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.slope = (p1[1]-p2[1]) / (p1[0]-p2[0])
        self.intercept = p1[1] - self.slope * p1[0]
        self.line = lambda x: self.slope * x + self.intercept
    
    def draw(self, array):
        
        plt.plot(array,self.line(array))

    def __eq__(self,other):
        if self.slope == other.slope and self.intercept == other.intercept:
            return True
        else:
            return False
xs = np.arange(0,10)
ys = (xs - 4)**2 + 1
plt.plot(xs,ys)
newb = line((3,4),(1,-1))
arr = np.arange(10)
newb.draw(arr)