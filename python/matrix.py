import random
from math import floor
import re


class Matrix:
    def __init__(self, alist=[[1]]):
        self.list = alist
        for each_row in self.list:
            assert len(each_row) == len(self.list[0]), "the matrix is not a rectangle"
        
        self.align = "center"
        self.dim = (len(self.list), len(self.list[0]))

    def __str__(self):
        """
        makes a string of self.list in an apealing way
        """
        #makes a matrix of strings of the values of the original mat
        string_mat = []
        for i in range(self.dim[0]):
            string_mat.append([])
            for j in range(self.dim[1]):
                string_mat[len(string_mat) - 1].append(str(self.list[i][j]))
                #this_row += [str(element)]
            #string_mat += [this_row]
        
        #makes a list of the max length of each column so they can be lined up well
        #also makes a list of bools whether or not there are any negatives in the list
        lengths = []
        negatives = []
        for col_index in range(self.dim[1]):

            max_length = len(string_mat[0][col_index])
            minus = bool(self.list[0][col_index] < 0)

            if self.dim[1] > 1:
                for row_index in range(1, self.dim[0]):
                    string = string_mat[row_index][col_index]
                    length = len(string)

                    if max_length < length:
                        max_length = length

                    if self.list[row_index][col_index] < 0:
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
        for y in range(self.dim[0]):
            for x in range(self.dim[1]):

                if negatives[x] and (self.list[y][x] >= 0) and len(string_mat[y][x]) > lengths[x]:
                    string_mat[y][x] = " " + string_mat[y][x]
                
                count = 0
                while len(string_mat[y][x]) < lengths[x]:
                    if re.search("^\s*[rR]",self.align):
                        string_mat[y][x] = " " + string_mat[y][x]

                    elif re.search("^\s*[lL]",self.align):
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

    def __add__(self, other):
        assert self.dim == other.dim, "matrix dimension error"

        out = []
        for y in range(self.dim[0]):
            row = []
            for x in range(self.dim[1]):
                row.append(self.list[y][x] + other.list[y][x])
            out += [row]
        
        return Matrix(out)
    
    def __mul__(self, other):
        assert self.dim[1] == other.dim[0], "width of first matrix is different from the height of the second"
        def entire(row=0):
            def across(col=0):
                def each(i=0):
                    if i == other.dim[0]:
                        return 0
                    return self.list[row][i] * other.list[i][col] + each(i + 1)
                if col == other.dim[1]:
                    return []
                return [each()] + across(col + 1)
            if row == self.dim[0]:
                return []
            return [across()] + entire(row + 1)
        return Matrix(entire())

    def __eq__(self, other):
        return bool(self.list == other.list)
    
    def scalar(self, scalar):
        return Matrix([[elem * scalar for elem in row] for row in self.list])
        
    def transpose(self):
        """
        transposes the matrix
        """
        if self.list != [] and self.list != [[]]:
            outmat = []
            for coli in range(self.dim[1]):
                newrow = []
                for rowi in range(self.dim[0]):
                    newrow += [self.list[rowi][coli]]
                outmat += [newrow]
            return Matrix(outmat)

    def rotate(self, how_many_times = 1):
        """
        rotates a matrix (arg1) a number of times (arg2):
        """
        how_many_times %= 4
        matter = self.list
        while 0 < how_many_times:
            how_many_times -= 1
            new_mat = []
            i = len(matter[0])
            while i > 0:
                i -= 1

                row = []
                for j in range(len(matter)):
                    row += [matter[j][i]]
                new_mat += [row]
            matter = new_mat
        return Matrix(matter)
    
    def reflectVert(self):
        return self.rotate(-1).transpose()

    def reflectHoriz(self):
        return self.rotate(1).transpose()

    def printAlign(self, align="center"):
        self.align = align

    def submatrix(self, row, col):
        """
        returns a submatrix deleting the specified row and the column
        if either are outside of range(dim) it will not be deleted
        """
        outmat = []
        for y in range(self.dim[0]):
            if y != row:
                outrow = []
                for x in range(self.dim[1]):
                    if x != col:
                        outrow += [self.list[y][x]]
                outmat += [outrow]
        return Matrix(outmat)
    
    def supermatrix(self, row, col):
        """
        undoes the effects of submatrix
        """
        outmat = [[0 for j in range(self.dim[1] + 1)] for i in range(self.dim[0] + 1)]
        for y in range(self.dim[0]):
            for x in range(self.dim[1]):
                outmat[y if y < row else y + 1][x if x < col else x + 1] = self.list[y][x]
        return Matrix(outmat)
    
    def det(self):
        """
        Returns the determinant as a scalar
        """
        assert self.dim[0] == self.dim[1], "matrix must be a square"

        if self.dim == (1,1):
            return self.list[0][0]
        else:
            return sum([(1 - 2*(i%2)) * self.list[0][i] * self.submatrix(0,i).det() for i in range(self.dim[1])])
    
    def identity(self,dimension):
        self.__init__([[1 if x==y else 0 for x in range(dimension)] for y in range(dimension)])
        return self
    


if __name__ == "__main__":
    def lrand():
        return int(random.random() * 10)
    unmat = Matrix([[88,80,25],[96,86,26],[56,44,9]])
    print(unmat)
    print("determinant of above matrix: {0}".format(unmat.det()))
    test = [Matrix([[lrand() for i in (0,1,2)] for j in (0,1)]) for k in (0,1)]
    print(test[0])
    print("~")
    print(test[0].scalar(2))
    print("~")
    print(test[1])
    print("~")
    print(test[0] * test[1].transpose())
    print("~")
    newmat = test[1].transpose() * test[0]
    print(newmat)
    print("~")
    print(Matrix().identity(5))