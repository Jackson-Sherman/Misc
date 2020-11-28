from PIL import Image
import numpy as np

class ErrorMatrix:

    def __init__(self, data):
        """
        data is a list in the form [[0,True,7],[3,5,1]] where True is the center is 
        """
        if isinstance(data, int) or isinstance(data, float) or isinstance(data, bool):
            self.mat = [[data,],]
        elif isinstance(data[0], int) or isinstance(data[0], float) or isinstance(data[0], bool):
            self.mat = [data,]
        else:
            self.mat = data
        
        self.size = (len(data), len(data[0]))
        found_yet = False
        for y in range(self.size[0]):
            for x in tuple(list(range(self.size[1])).reverse()):
                if found_yet:
                    self.mat[y][x] = 0
                if not (isinstance(self.mat[y][x], int) and isinstance(self.mat[y][x], float)):
                    self.center = (y,x)
                    found_yet = True

        self.mat = self.mat[self.center[0]:]



bina = []
for i in (0, 1):
    for j in (0, 1):
        bina += [(i,j)]
bina = tuple(bina)
print("¬X ∨ ¬Y")
for each in bina:
    print("(X,Y):{0}, out:{1}".format(each, 1 if not(bool(each[0]) and bool(each[1])) else 0))
print(bina)
mat = [
    [0, True, 7],
    [3, 5, 1]
]

print(mat)

def acting(string):
    infile = Image.open(string)
    size = infile.getbbox()[2:]
    px = infile.load()
    print(size)
    array = np.empty([size[0],size[1]])
    print(type(array))
    for y in range(size[0]):
        for x in range(size[1]):
            array[y][x] = px[x, y]

    def closest(value):
        cutoff = 128
        return 0 if value < cutoff else 255

    for y in range(size[0]):
        if y%2 == 0:
            d = 1
            dire = range(size[1])
        else:
            d = -1
            dire = range(size[1] - 1, -1, -1)
        
        for x in dire:
            old = array[y][x]
            new = closest(old)
            array[y][x] = new
            q = old - new
            if x+d < size[1]:
                array[y][x + d] += q * 7/16
            if x+d < size[1] and y+1 < size[0]:
                array[y + 1][x + d] += q * 1/16
            if y+1 < size[0]:
                array[y + 1][x] += q * 5/16
            if x-d < size[1] and y+1 < size[0]:
                array[y + 1][x - d] += q * 3/16



    return Image.fromarray(array)

copy = acting("/Users/jacksonsherman/Downloads/reputation.png")
copy.show()