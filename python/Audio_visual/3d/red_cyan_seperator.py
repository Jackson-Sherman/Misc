from PIL import Image
import numpy as np

real_path = input("\nType file path or press return for default: ")
if not real_path:
    real_path = ''

def seperate(path):
    print(path)
    inp = Image.open(path)
    px = inp.load()
    size = inp.getbbox()[2:]
    orig = np.empty((*size,3))
    l = 'l'
    r = 'r'
    rgb = 'rgb'
    baw = 'baw'
    out = {
        rgb: {
            l: inp.copy(),
            r: inp.copy()
        },
        baw: {
            l: inp.copy(),
            r: inp.copy()
        }
    }
    out[rgb][l] = out[rgb][l].convert(mode='RGB', matrix=(
        1.0,0.0,0.0,0.0,
        0.0,0.0,0.0,0.0,
        0.0,0.0,0.0,0.0,
    ))
    out[rgb][r] = out[rgb][r].convert(mode='RGB', matrix=(
        0.0,0.0,0.0,0.0,
        0.0,1.0,0.0,0.0,
        0.0,0.0,1.0,0.0,
    ))
    out[baw][l] = out[baw][l].convert(mode='L', matrix=(1.0,0.0,0.0,0.0))
    out[baw][r] = out[baw][r].convert(mode='L', matrix=(0.0,0.5,0.5,0.0))
    out[px] = {
        rgb: {
            l: out[rgb][l].load(),
            r: out[rgb][r].load()
        },
        baw: {
            l: out[baw][l].load(),
            r: out[baw][r].load()
        }
    }
    w = 16*size[1]/9-size[0]
    if w < 0:
        w = 0
    elif w % 1 == 0:
        w = int(w)
    else:
        w = int(w+0.5)
    s_x,s_y = size
    array = 'array'
    im = 'im'
    big = {
        array: {
            rgb: np.empty((2*s_y, 2*s_x + w),tuple),
            baw: np.empty((2*s_y, 2*s_x + w),int)
        }
    }
    big[array][rgb].fill((0,0,0))
    big[array][baw].fill(0)
    def chopit(s,ext=''):
        if s[-1] == '.':
            return s[:-1],'.'+ext
        else:
            return chopit(s[:-1],s[-1]+ext)

    pa,th = chopit(path)

    print('|                    |\n|',end='')
    for key in (rgb,baw):
        for y in range(s_y):
            for x in range(s_x):
                big[array][key][  2 * y  ][     x     ] = out[px][key][l][x, y]
                big[array][key][  2 * y  ][w + x + s_x] = out[px][key][r][x, y]
                big[array][key][2 * y + 1][     x     ] = out[px][key][l][x, y]
                big[array][key][2 * y + 1][w + x + s_x] = out[px][key][r][x, y]
            if y%(s_y/10) > (y+1)%(s_y/10):
                print('#',end='')
        big[im][key] = Image.fromarray(big[array][key])
        bik[im][key].save(pa+'_big_'+key+th)
    print('|')

def run(string):
    s = string.split(';')
    for each in s:
        seperate(each)
if real_path:
    run(real_path)