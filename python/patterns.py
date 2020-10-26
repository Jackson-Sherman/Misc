d = {
    ((0,0),(0,0)): " ",
    ((1,0),(0,0)): "▘",
    ((0,1),(0,0)): "▝",
    ((1,1),(0,0)): "▀",
    ((0,0),(1,0)): "▖",
    ((1,0),(1,0)): "▌",
    ((0,1),(1,0)): "▞",
    ((1,1),(1,0)): "▛",
    ((0,0),(0,1)): "▗",
    ((1,0),(0,1)): "▚",
    ((0,1),(0,1)): "▐",
    ((1,1),(0,1)): "▜",
    ((0,0),(1,1)): "▄",
    ((1,0),(1,1)): "▙",
    ((0,1),(1,1)): "▟",
    ((1,1),(1,1)): "█"
}
lalista = [((i%2,(i//2)%2),((i//4)%2,(i//8)%2)) for i in range(16)]
def concat(listofstrings):
    if listofstrings:
        char = listofstrings.pop()
        return concat(listofstrings) + char
    else:
        return ""
def cycle(lista,cuanto=-1):
    if cuanto == -1:
        return [lista[cuanto]] + lista[:cuanto]
    elif cuanto == 1:
        return lista[cuanto:] + [lista[cuanto-1]]
    elif cuanto < 0:
        return lista[cuanto:] + lista[:cuanto]
    elif cuanto > 0:
        return lista[cuanto:] + lista[:cuanto]
    else:
        return lista
print(concat(list(d.values())))
for i in range(15):
    print(concat(cycle(list(d.values()),i)))
for i in range(16):
    print("~~~~~~~~~~\n{}: {}\n{}".format(lalista[i][0], d[lalista[i]],lalista[i][1]))

def draw(mat):
    oldmat = mat
    if len(mat) % 2 == 1:
        mat += [[0 for i in range(len(mat[0]))]]
    if len(mat[0]) % 2 == 1:
        for i in range(len(mat)):
            mat[i] += [0]
    newmat = []
    for i in range(len(mat)//2):
        row = []
        for j in range(len(mat[0])//2):
            minimat = (
                (mat[i*2+0][j*2+0], mat[i*2+0][j*2+1]),
                (mat[i*2+1][j*2+0], mat[i*2+1][j*2+1])
            )
            row += [minimat]
        newmat += [row]
    dastring = ""
    for eachrow in newmat:
        for elem in eachrow:
            dastring += d[elem]
        if eachrow != newmat[-1]:
            dastring += "\n"
    mat = oldmat
    print(dastring)
draw([
    [1,1,1,1],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,0,1]
])