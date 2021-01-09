import math
class Bin:
    def __init__(self, val):
        if isinstance(val, str):
            if val[0] == "-":
                self.neg == True
            self.v = val
        else:
            self.v = ""
            if val < 0:
                self.neg = True
                val *= -1
            else:
                self.neg = False

            if isinstance(val, float):
                self.frac = val - int(val)
                val = int(val)
            elif isinstance(val, int):
                self.frac = 0.0
            
            x = 31
            while 0 < val:
                if val < 2**x:
                    self.v += "0"
                else:
                    self.v += "1"
                    val -= 2**x
                x -= 1
            self.v += "0"*(x+1)

    def get_bit(self, index):
        return int(self.v[31-index])
    
    def set_bit(self, index, value):
        self.v = self.v[:31-index] + str(value) + self.v[32-index:]
    
    def __add__(self, other):
        i = 0
        c = 0
        out = Bin(0)
        while i < 32:
            bits = (self.get_bit(i), other.get_bit(i), c)
            if bits == (0,0,0):
                out.set_bit(i,0)
                c = 0
            
            elif bits == (0,0,1) or bits == (0,1,0) or bits == (1,0,0):
                out.set_bit(i,1)
                c = 0

            elif bits == (1,1,0) or bits == (1,0,1) or bits == (0,1,1):
                out.set_bit(i,0)
                c = 1

            elif bits == (1,1,1):
                out.set_bit(i,1)
                c = 1
            i += 1
        return out

    def __str__(self):
        s = self.v
        if s != "0"*32:
            while s[0] == "0":
                s = s[1:]
        else:
            s = "0"
        if self.neg:
            s = "-" + s
        return s

if __name__ == "__main__":
    x = Bin(4)
    y = Bin(4)
    z = x+y
    print(z)