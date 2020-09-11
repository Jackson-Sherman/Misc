import math
from PIL import Image

def testdif(old):
    oldpx = old.load()

    img = Image.new("RGB", old.size, "black")
    px = img.load()

    array = []

    for x in range(img.size[0]):
        array.append([])
        for y in range(img.size[1]):
            px[x, y] = oldpx[x, y]
            array[x].append(list(px[x, y]))


    
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            oldpx = array[x][y]
            newpx = []

            is_dark = bool(max(oldpx[0], oldpx[1], oldpx[2]) + min(oldpx[0], oldpx[1], oldpx[2]) < 256)

            if is_dark:
                newpx = [0, 0, 0]
            
            else:
                newpx = [255, 255, 255]

            array[x][y] = newpx
            px[x, y] = tuple(array[x][y])

    return img

    


def errorDiff(old):
    oldpx = old.load()
    maxy = 0
    miny = 256
    for x in range(old.size[0]):
        for y in range(old.size[1]):
            for i in (0,1,2):
                maxy = max(maxy, oldpx[x, y][i])
                miny = min(miny, oldpx[x, y][i])

    print(miny)
    print(maxy)

    img = Image.new("RGB", old.size, "black")
    px = img.load()

    array = []

    for x in range(img.size[0]):
        array.append([])
        for y in range(img.size[1]):
            px[x, y] = oldpx[x, y]
            array[x].append(list(px[x, y]))
    
    mat = [
        [0, 0, 7], 
        [3, 5, 1]
    ]

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            oldpx = array[x][y]
            newpx = []

            is_dark = bool(max(oldpx[0], oldpx[1], oldpx[2]) + min(oldpx[0], oldpx[1], oldpx[2]) < 256)

            if is_dark:
                newpx = [miny, miny, miny]
            
            else:
                newpx = [maxy, maxy, maxy]

            array[x][y] = newpx
            px[x, y] = tuple(array[x][y])

            temp_mat = list()
            total = 0

            for i in (0,1,2):
                temp_mat.append(list())

                for row in range(len(mat)):
                    temp_mat[i].append(list())

                    for col in range(len(mat[row])):
                        temp_mat[i][row].append(mat[row][col] * (oldpx[i] - newpx[i]))
                        total += mat[row][col]

            total /= 3

            med = int(len(mat[row]) / 2)
            c = med

            while x < c:
                for i in (0,1,2):
                    for row in range(len(temp_mat[i])):
                        total -= mat[row][med - c] / 3
                        temp_mat[i][row][med - c] = 0

                c -= 1
            
            c = med

            while img.size[0] <= x + c:
                for i in (0,1,2):
                    for row in range(len(temp_mat[i])):
                        total -= mat[row][med + c] / 3
                        temp_mat[i][row][med + c] = 0

                c -= 1

            c = len(temp_mat[0])

            while img.size[1] < y + c:
                for i in (0,1,2):
                    for col in range(len(temp_mat[i][c - 1])):
                        total -= mat[c - 1][col]/3
                        temp_mat[i][c - 1][col] = 0
                c -= 1

            for i in (0,1,2):
                for r in range(len(temp_mat[i])):
                    for c in range(len(temp_mat[i][r])):
                        temp_mat[i][r][c] /= total

            if x == 80 and y == img.size[1] - 1:
                print(temp_mat[0])
                k = 0
                for r in range(len(temp_mat[i])):
                    for c in range(len(temp_mat[i][r])):
                        k += temp_mat[0][r][c]

                print(k)
                print(oldpx[0] - newpx[0])

            for row in range(len(mat)):
                domain = range(len(mat[row]))

                if row == 0:
                    domain = range(int(len(mat[row]) / 2) + 1, len(mat[row]))

                if y + row < img.size[1]:
                    for col in domain:
                        if 0 <= x + col - int(len(mat[row]) / 2) and x + col - int(len(mat[row]) / 2) < img.size[0]:
                            for i in (0,1,2):
                                array[x + col - int(len(mat[row]) / 2)][y + row][i] += temp_mat[i][row][col]
                                if array[x + col - int(len(mat[row]) / 2)][y + row][i] < miny:
                                    array[x + col - int(len(mat[row]) / 2)][y + row][i] = miny
                                elif maxy < array[x + col - int(len(mat[row]) / 2)][y + row][i]:
                                    array[x + col - int(len(mat[row]) / 2)][y + row][i] = maxy

    return img



def gauss(img, sdev):

    def gus(x):
        x /= sdev
        x **= 2
        x /= -2
        x = math.exp(x)
        x /= sdev * (2 * math.pi) ** 0.5
        return x

    mat = [gus(0)]
    total = gus(0)
    many = 0

    while total < 0.95:
        many += 1
        out = gus(many)
        total += 2 * out
        mat.append(out)
        mat.insert(0, out)
    
    for x in range(len(mat)):
        mat[x] /= total
    
    imgpx = img.load()

    output = Image.new("RGB", tuple(img.size), "black")
    outpx = output.load()

    
    for x in range(output.size[0]):
        for y in range(output.size[1]):
            outpx[x, y] = imgpx[x, y]

    for y in range(output.size[1]):
        for x in range(output.size[0]):
            total = [0, 0, 0]

            for c in range(len(mat)):
                toCheck = x + c - int(len(mat) / 2)

                if toCheck < 0:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[0, y][each]

                elif output.size[0] <= toCheck:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[img.size[0] - 1, y][each]

                else:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[toCheck, y][each]

            for each in (0,1,2):
                total[each] = int(total[each])
            
            outpx[x,y] = tuple(total)

    for x in range(output.size[0]):
        for y in range(output.size[1]):
            total = [0, 0, 0]

            for c in range(len(mat)):
                toCheck = y + c - int(len(mat) / 2)
                
                if toCheck <= 0:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[x, 0][each]

                elif output.size[1] - 1 <= toCheck:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[x, output.size[1] - 1][each]

                else:
                    for each in (0,1,2):
                        total[each] += mat[c] * outpx[x, toCheck][each]

            for each in (0,1,2):
                total[each] = int(total[each])
            
            outpx[x, y] = tuple(total)

    return output