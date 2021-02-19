from PIL import Image
import numpy as np
import datetime

"""
in this program, points will be ordered x then y
"""

# print("for the following, just press retrun if the given defaults are what you want, else type it as a tuple")
s = "" # input("Is a frame size of (1280, 720) ok?: ")
if not s:
    s = "1280, 720"
frame = eval(s)

s = "" # input("Is a banner size of (1800, 156) ok?: ")
if not s:
    s = "1800, 156"
banner = eval(s)

class Vect:
    def __init__(self,x=None,y=None,t=int,offset=False):
        if isinstance(x,complex):
            self.x, self.y = x.real, x.imag
        elif isinstance(x,tuple):
            self.x, self.y = x
        else:
            try:    self.x = t(x)
            except: self.x = t(0)
            
            try:    self.y = t(y)
            except: self.y = t(0)
    
    def __getitem__(self, i):
        try:
            if int(i) == 0:
                return self.x
            if int(i) == 1:
                return self.y
        finally:
            assert i*i == i, "i must be either equal to 0 or 1"
    
    def __add__(self,other):
        return Vect(*[self[i] + other[i] for i in range(len(self))])
    def __radd__(self,other):
        return Vect(*[other[i] + self[i] for i in range(len(self))])
    def __iadd__(self,other):
        self.x,self.y = self.x + other[0], self.y + other[1]

    def __sub__(self,other):
        return Vect(*[self[i] - other[i] for i in range(len(self))])
    def __rsub__(self,other):
        return Vect(*[other[i] - self[i] for i in range(len(self))])
    def __isub__(self,other):
        for i in range(len(self)):
            self[i] = self[i] - other[i]

    def __truediv__(self,other):
        return self.scale(1/other)

    def __mul__(self,other):
        return self.scale(other)

    def __rmul__(self,other):
        return self.scale(other)

    def scale(self, other):
        if isinstance(other, (int,float)):
            return Vect(*[int(self[i] * other+0.5) for i in range(len(self))])

    def within(self,box):
        tl,br = None,None
        if len(box) == 4:
            tl = Vect(*box[:2])
            br = Vect(*box[2:])
        elif len(box) == 2:
            if not isinstance(box[0],Vect):
                tl = Vect(*[box[0][i] for i in range(len(box[0]))])
            else:
                tl = box[0]
            if not isinstance(box[1],Vect):
                br = Vect(*[box[1][i] for i in range(len(box[1]))])
            else:
                br = box[1]
        assert self.x >= tl.x, "x value is too small"
        assert self.x <  br.x, "x value is too large"
        assert self.y >= tl.y, "y value is too small"
        assert self.y <  br.y, "y value is too large"
        

    def offsetx(self):
        return int(self.x + int(int(self.y / bs.y) * bs.y * d.x / d.y + 0.5))
    
    def offset(iny):
        return int(int(iny / bs.y) * bs.y * d.x / d.y + 0.5)
    
    def incr(self):
        self += d
    
    def __len__(self):
        return 2
    
    def __str__(self):
        return "⟨" + str(self.x) + "," + str(self.y) + "⟩"

fs = Vect(*frame)  # fs for frame size
bs = Vect(*banner) # bs for banner size


filepath = "Desktop/banners/original.png"
orig = Image.open(filepath)
x,y = "xy"
dx,dy = "dx","dy"
now = lambda: datetime.datetime.now()
previous = now()
def time2micro(t):
    if isinstance(t,datetime.time):
        output = 0
        output += t.hour
        output *= 60
        output += t.minute
        output *= 60
        output += t.second
        output *= 1000000
        output += t.microsecond
        return output
    else:
        return 0
def diff(tp,ti):
    microtp = time2micro(tp.time())
    microti = time2micro(ti.time())
    output = microtp - microti
    string = "hrs "
    output /= 1000000 # now in seconds
    string += "{:0>2}:".format(int(output/60/60))
    if output < 60*60:
        string = "   mins "
    string += "{:0>2}:".format(int(output/60))
    if output < 60:
        string = "      secs "
    string += "{:0>9.6f}".format(output)
    return string[:-3] + " " + string[-3:]

def ima(now):
    global previous
    output, previous = diff(now,previous), now

    return output

def rpath(string):
    if string[-1] == "/":
        return string
    else:
        return rpath(string[:-1])

def suffix(string):
    if string[-1] == ".":
        return "."
    else:
        return suffix(string[:-1]) + string[-1]

opath = rpath(filepath), suffix(filepath)

def result(name):
    name = str(name)
    if len(name) < 2:
        return result("0" + name)
    
    return opath[0] + name + opath[1]

d = Vect(1,2)
# oarr = np.array(orig)
# print(oarr.shape)
# shape = Vect(oarr.shape[1],oarr.shape[0])
# count = oarr.shape[0] // bs.x
# for i in range(1,count+1):
#     newimg = Image.fromarray(oarr[(i - 1) * bs.y : i * bs.y],"RGBA")
#     newimg.save(result(i))
#     print("done with season {:>}".format(i))
# 
# print("ok, moving on")
# 
# assert bs.y%(d.x/d.y) == 0
# 
# each_offset = (bs.y * d.x)//d.y
# 
# loc = Vect(each_offset * (fs.y//bs.y),0)
# print(Vect.offset(0))
# rsize = Vect((shape-Vect(1,1)).offsetx(),shape.y-1)+Vect(1,1)
# rarr = np.ndarray((rsize.y, rsize.x, oarr.shape[2]),int)
# rarr.fill(255)
# po = Vect(0,0)
# pr = Vect(0,0)
# outarr = np.pad(oarr[:bs.y],((0,0),(0,Vect.offset(shape.y-2)),(0,0)),constant_values=((0,0),(255,255),(0,0)))
# print("done with 1")
# for i in range(1, oarr.shape[0]//bs.y):
#     ov = Vect.offset(bs.y*i)
#     offset = ov, Vect.offset(shape.y - 2) - ov
#     outarr = np.concatenate((
#         outarr,
#         np.pad(
#             oarr[bs.y*i:bs.y*(i+1)],
#             (
#                 (0,0),
#                 offset,
#                 (0,0)
#             ),
#             constant_values=(
#                 (0,0),
#                 (255,255),
#                 (0,0)
#             )
#         )
#     ))
#     print("done with " + str(1+i))
# 
# rimg = Image.fromarray(outarr,"RGBA")
# rimg.save(result("offset"))
# rimg.show()



# orimg = Image.open(result("offset"))
# oarr = np.array(orimg)
# outarr = np.pad(
#     oarr,
#     (
#         (0,0),
#         ((oarr.shape[1] - bs.x) // 2+bs.y//4,)*2,
#         (0,0)
#     ),
#     constant_values=(
#         (0,0),
#         (255,255),
#         (0,0)
#     )
# )
# outarr = np.concatenate((
#     np.pad(
#         np.roll(oarr[oarr.shape[0] // 2:], 2*(bs.x - oarr.shape[1])-bs.y),
#         (
#             (0,0),
#             (0,oarr.shape[1] - bs.x+bs.y//2),
#             (0,0)
#         ),
#         constant_values=(
#             (0,0),
#             (255,255),
#             (0,0)
#         )
#     ),
#     outarr
# ))
# outarr = np.concatenate((
#     outarr,
#     np.pad(
#         np.roll(oarr[:oarr.shape[0] // 2], 2*(oarr.shape[1] - bs.x)+bs.y),
#         (
#             (0,0),
#             (oarr.shape[1] - bs.x+bs.y//2,0),
#             (0,0)
#         ),
#         constant_values=(
#             (0,0),
#             (255,255),
#             (0,0)
#         )
#     )
# ))
# newim = Image.fromarray(outarr)
# newim.save(result("double_offset"))
# newim.show()


oimg = Image.open(result("double_offset"))
def rect(cntr):
    corners = cntr - fs/2, cntr + fs/2
    newbox = oimg.getbbox()
    newbox = newbox[:2] + (newbox[2]+1,) + (newbox[3]+1,)
    corners[0].within(newbox)
    corners[1].within(newbox)
    return corners[0].x,corners[0].y,corners[1].x,corners[1].y

point = Vect(bs.x//2,oimg.getbbox()[3] // 4 + bs.y // 2)
point.x = point.offsetx()
end = 3 * oimg.getbbox()[3] // 4 + bs.y // 2
cnt = 1
start = oimg.crop(rect(point))
print("\n    done with 1")
point.incr()
cnt += 1
frames = []
previous = now()
starts = (oimg.getbbox()[3] // 4 + bs.y // 2)
perc = lambda: "{:>4.0f}".format(1000*(point.y-starts)/(end-starts))
while point.y < end:
    frames.append(oimg.crop(rect(point)))
    print(ima(now())+" " + perc() + " done with " + str(cnt))
    for i in range(4):
        point.incr()
    cnt += 1
print("\n\n" + "*"*20 + "\n\nNow saving final image...\n\n")
previous = now()
start.save(result("temp"),save_all=True,append_images=frames,duration=33)
print(ima(now())+" - done")