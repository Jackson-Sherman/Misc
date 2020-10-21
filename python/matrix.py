import random
from math import floor
import re

mat_in = [
    [-5,25,-125],
    [-4,16,-64],
    [-3,9,-27],
    [-2,4,-8],
    [-1,1,-1],
    [0,0,0],
    [1,1,1],
    [2,4,8],
    [3,9,27],
    [4,16,64],
    [5,25,125]
]

mat_test = [
    [-34745,-1737,87318,7,],
    [296,74,605,-2,],
    [-56093,-5008,-73,6,],
    [-27,-459,0,-829,],
    [-79867,5215,-760,-7,],
    [-5096,-2,6445,22,],
    [5822,-96,2,8,],
]
mat_test1 = [
    [1,22,1,22,],
    [22,4444,22,4444,],
    [1,22,-1,-22,],
    [22,4444,-22,-4444,],
]


def toString(mat, align = "center"):
    """
    prints mat in an apealing way
    """
    height = len(mat)
    width = len(mat[0])
    #makes a matrix of strings of the values of the original mat
    string_mat = []
    for i in range(height):
        string_mat.append([])
        for j in range(width):
            string_mat[len(string_mat) - 1].append(str(mat[i][j]))
            #this_row += [str(element)]
        #string_mat += [this_row]
    
    #makes a list of the max length of each column so they can be lined up well
    #also makes a list of bools whether or not there are any negatives in the list
    lengths = []
    negatives = []
    for col_index in range(width):

        max_length = len(string_mat[0][col_index])
        minus = bool(mat[0][col_index] < 0)

        if width > 1:
            for row_index in range(1, height):
                string = string_mat[row_index][col_index]
                length = len(string)

                if max_length < length:
                    max_length = length

                if mat[row_index][col_index] < 0:
                    minus = True

        lengths += [max_length]
        negatives += [minus]

    def num2let(num):
        num = int(num)
        num %= 52
        littlestring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        out = littlestring[num]
        return out

    #uses the above list to actually line it up
    for y in range(height):
        for x in range(width):

            if negatives[x] and (mat[y][x] >= 0) and len(string_mat[y][x]) > lengths[x]:
                string_mat[y][x] = " " + string_mat[y][x]
            
            count = 0
            while len(string_mat[y][x]) < lengths[x]:
                if re.search("^\s*[rR]",align):
                    string_mat[y][x] = " " + string_mat[y][x]

                elif re.search("^\s*[lL]",align):
                    string_mat[y][x] = string_mat[y][x] + " "

                else:
                    if count % 2 == 0:
                        string_mat[y][x] = " " + string_mat[y][x]
                    else:
                        string_mat[y][x] = string_mat[y][x] + " "
                

                count += 1
    
    #makes a list of strings of each row of the matrix for printing
    string_list = []
    string = ""
    for i, row in enumerate(string_mat):
        if len(string_mat) == 1:
            string += "("
        elif i == 0:
            string += "⎛"
        elif i + 1 < len(string_mat):
            string += "⎜"
        else:
            string += "⎝"
        
        for j, value in enumerate(row):
            string += str(value)
            string += " " * 2
        string = string[:-2]

        if len(string_mat) == 1:
            string += ")"
        elif i == 0:
            string += "⎞\n"
        elif i + 1 < len(string_mat):
            string += "⎟\n"
        else:
            string += "⎠"

    return string

def print_mat(lemat, lalign="center"):
    print(toString(lemat,lalign))

def rotate(mat, how_many_times = 1):
    """
    rotates a matrix (arg1) a number of times (arg2):
    """
    how_many_times %= 4
    matter = mat
    for times in range(how_many_times):
        new_mat = []
        i = len(matter[0])
        while i > 0:
            i -= 1

            row = []
            for j in range(len(matter)):
                row += [matter[j][i]]
            new_mat += [row]
        matter = new_mat
    return matter
    
def reflect(mat, direction = 0):
    def true_direction(dire):
        if type(dire) == type(0) or type(dire) == type(0.5) or type(dire) == type(3 +2j) or type(dire) == type(True):
            if dire:
                return True
            else:
                return False

        if re.search("\s*^(0|[lLrR])",dire):
            pass
    if direction:
        pass


def multiply(matA, matB="na"):
    def entire(row=0):
        if row == len(matA):
            return []
        else:
            def across(col=0):
                if col == len(matB[0]):
                    return []
                else:
                    def each(i=0):
                        if i == len(matB):
                            return 0
                        else:
                            return matA[row][i] * matB[i][col] + each(i + 1)

                    return [each()] + across(col + 1)

            return [across()] + entire(row + 1)

    try:
        if matB == "na":
            matB = matA[1]
            matA = matA[0]
        return entire()
    except:
        print("error :( sorry")
            

test = [
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1],
    ],
    [
        [0,0,1,1],
        [0,1,0,1]
    ],
    [
        [0,1,0,1],
        [0,0,1,1]
    ]
]
listy = [re.split("\n",toString(test[i])) for i in (0,1)]
for i in range(len(listy[0])):
    pass
print_mat(test[0])
print_mat(test[1])
print_mat(multiply(test[0],test[1]))
print_mat(multiply(test[0],test[2]))



mat_out = rotate(mat_in,1)

print(mat_in)
print(mat_out)

print("\n  ~  ~~ ~~~ ~~  ~  \n")

print_mat([[0,1]])
print("")
print_mat(mat_in)
print("")
print_mat(mat_out)

print("\n  ~  ~~ ~~~ ~~  ~  \n")

print_mat(mat_test)
print("")
print_mat(rotate(mat_test,-1))
print("")
print_mat(mat_test)