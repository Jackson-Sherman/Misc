c = input("enter value for c:")

prevs = [0j]
z = c

loopCount = 0
print("cycles: {}, z = {}".format(loopCount, 0))

while z not in prevs:
    loopCount += 1
    print("cycles: {}, z = {}".format(loopCount, z))
    prevs.append(z)
    z **= 2
    z += c
    