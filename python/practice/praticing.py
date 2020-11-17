import numpy as np

import sys
sys.path.insert(1,"/Users/jacksonsherman/VSC/Misc/python")
from matrix import Matrix

graph = Matrix([
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,0],
    [0,1,0,0]
])

print(graph)
print("\t that graph squared is:")
square = graph ** 2
print(square)
print("\t that graph squared is:")
square = square ** 2
print(square)