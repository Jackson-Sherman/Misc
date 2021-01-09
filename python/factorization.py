value = int(input("Number to be factorized:"))
original = value
sqrtoriginal = original ** 0.5
print(str(value), end=": ")
i = 2
output = []
first = True
while 1 < value:
    while value % i == 0:
        if first:
            first = False
            print(str(i), end="")
        else:
            print(", " + str(i), end="")
        output += [i]
        value /= i
    i += 2 if i > 2 else 1
print()
print("done")