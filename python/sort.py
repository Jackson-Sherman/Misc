import random
import time
import math
xlst = [int(random.random()*90)+10 for i in range(4)]

def insertion(lst, rando=False):
    if rando:
        last = lst[-1]
        params = (1, len(lst))
        while lst[0] != last:
            r = random.randint(*params)
            lst = lst[1:r] + [lst[0]] + lst[r:]
        r = random.randint(*params)
        lst = lst[1:r] + [lst[0]] + lst[r:]
        return lst
    else:
        output = []
        while 1 < len(lst):
            mini = 0
            for i in range(1, len(lst)):
                if lst[i] < lst[mini]:
                    mini = i
            if lst[mini] != lst[-1]:
                output.append(lst[mini])
                lst = lst[:mini] + lst[mini+1:]
            else:
                output.append(lst[mini])
                lst = lst[:mini]
        output.append(lst[0])
        return output

def bubble(lst, rando=False):
    def flip(ind,jnd):
        """
        inde
        """
        lst[ind], lst[jnd] = lst[jnd], lst[ind]
    if rando:
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if random.random() < 0.5:
                    flip(i,j)
        return lst
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                flip(i,j)
    return lst

def merge(lst):
    def merge_them(lst1, lst2):
        l = [len(lst1), len(lst2)]
        output = []
        while 0 < l[0] + l[1]:
            if 0 < l[0] * l[1]:
                if lst1[0] < lst2[0]:
                    output += lst1[0:1]
                    lst1 = lst1[1:]
                    l[0] -= 1
                elif lst1[0] > lst2[0]:
                    output += lst2[0:1]
                    lst2 = lst2[1:]
                    l[1] -= 1
                else:
                    output += lst1[0:1] + lst2[0:1]
                    lst1 = lst1[1:]
                    lst2 = lst2[1:]
                    l[0] -= 1
                    l[1] -= 1
            else:
                if l[0] == 0:
                    output += lst2[0:]
                    lst2 = []
                    l[1] = 0
                elif l[1] == 0:
                    output += lst1[0:]
                    lst1 = []
                    l[0] = 0
        return output
    
    # Do the rest, please, Jackson


    def recur(lst, lo, hi):
        if lo + 1 < hi:
            mid = int((lo + hi) / 2)
            recur(lst, lo, mid)
            recur(lst, mid, hi)
            merge_them(lst, lo, mid, hi)
        else:
            return lst[lo:hi]

def quick(lst):
    if len(lst) <= 1:
        return lst
    else:
        # def beforeAndAfter(xlst, left=[], right=[]):
        #     if len(xlst) < 1:
        #         return (left, right,)
        #     else:

        #         if xlst[0] <= xlst[-1]:
        #             return beforeAndAfter(xlst[1:], left+[xlst[0]], right)
        #         else:
        #             return beforeAndAfter(xlst[1:], left, right+[xlst[0]])
        # l, r = beforeAndAfter(lst)
        # return quick(l) + quick(r)
        check = lst[0]
        before = []
        after = []
        for i in range(1,len(lst)):
            if lst[i] <= check:
                before += [lst[i]]
            else:
                after += [lst[i]]
        return quick(before) + [check] + quick(after)

def heap(lst):
    class Heap:
        def __init__(self, value_list):
            self.heaps = value_list if isinstance(value_list, list) else list(value_list)
            self.l = len(value_list)
            self.rightmost = 2**int(math.log2((len(self)-1)+2.5)) - 2
        
        def __len__(self):
            return self.l
        
        def swap(self, index1, index2):
            self.heaps[index1], self.heaps[index2] = self.heaps[index2], self.heaps[index1]
        
        def parent(self, index):
            return int((index - 1) / 2)

        def l_child(self, index):
            val = 2 * index + 1
            if val < len(self):
                return val
            else:
                return False
        
        def r_child(self, index):
            val = 2 * index + 2
            if val < len(self):
                return val
            else:
                return False
        
        def children(self, index):
            if 2 * index + 2 < len(self):
                return (2 * index + 1, 2 * index + 2)
            elif 2 * index + 1 < len(self):
                return (2 * index + 1,)
            else:
                return ()

        def pop_and_sift(self):
            if 0 < len(self):
                if 1 < len(self):
                    output = self.heaps[0]
                    self.heaps = [self.heaps[-1]] + self.heaps[1:-1]
                    self.l -= 1
                else:
                    output = self.heaps[0]
                    self.heaps = []
                    self.l = 0
                self.siftDown(0)
                return output

        def sort(self):
            output = []
            while 0 < len(self):
                output = [self.pop_and_sift()] + output
            return output

        def hepify(self):
            start = self.parent(len(self) - 1)
            unvisited = [i for i in range(start,-1,-1)]
            for i in unvisited:
                self.siftDown(i)
        
        def siftDown(self, index):
            kids = self.children(index)
            if kids:
                if len(kids) < 2:
                    test = kids[0]
                else:
                    if self.heaps[kids[0]] > self.heaps[kids[1]]:
                        test = kids[0]
                    else:
                        test = kids[1]
                if self.heaps[test] > self.heaps[index]:
                    self.swap(test, index)
                    self.siftDown(test)
                else:
                    pass
        
        def __str__(self):
            data = [str(i) for i in self.heaps]
            lens = [len(i) for i in data]
            depth = 1
            cur = 0
            while self.children(cur):
                cur = self.children(cur)[0]
                depth += 1
            rows = ["" for i in range(depth)]

            def order_it(heap, current, order=[]):
                kids = heap.children(current)
                if heap.rightmost in order:
                    return tuple(order)

                if kids:
                    if kids[0] not in order:
                        return order_it(heap, kids[0], order)
                        
                    elif len(kids) > 1:
                        if current not in order and kids[1] not in order:
                            return order_it(heap, kids[1], order=order + [current,])
                        else:
                            return order_it(heap, heap.parent(current), order)
                    else:
                        if current not in order:
                            return order_it(heap, heap.parent(current), order=order + [current,])
                        else:
                            return order_it(heap, heap.parent(current), order)

                return order_it(heap, heap.parent(current), order=order + [current,])

            order = order_it(self, 0)
            for i in order:
                for n,r in enumerate(rows):
                    if 2**n < i+1.5 and i+1.5 < 2**(n+1):
                        rows[n] = r + data[i]
                    else:
                        rows[n] = r + " " * lens[i]
            output = "\n"
            while rows:
                output += rows[0] + "\n"
                rows = rows[1:]
            output = output[:-1]
            return output


    h = Heap(lst)
    h.hepify()
    lst = h.sort()
    return lst

l = [i for i in range(-9,100)]
start = time.time()
insertion(l,True)
stop = time.time()
print("time: {}".format(stop - start))
k = heap(l)
xlst = l
print(xlst)
print()
# def form(n):
#     if n < 0:
#         neg = "-"
#         n *= -1.0
#     else:
#         neg = " "
#         n *= 1.0
#     if 1 <= n and n < 1000:
#         if 1 <= n and n < 10:
#             if len(4 < str(n*1.0))
#             return neg + str(n)[:6]
#         return neg + 
import sqlite3

connection = sqlite3.connect("thisone.db")
c = connection.cursor()
c.execute("DROP TABLE IF EXISTS Funcs")
c.execute("""CREATE TABLE Funcs (Name text, Time real, Result text)""")
functions = (insertion, quick, bubble, heap)
for func in functions:
    l = xlst
    start = time.time()
    k = func(l)
    stop = time.time()
    t = stop - start
    order = ""
    while k:
        s = str(k[0])
        if len(s) < 2:
            if k[0] < 0:
                s = s[0] + "0"*(2-len(s)) + s[1:]
            else:
                s = "0"*(2-len(s)) + s
        order += s + ","
        k = k[1:]
    order = order[:-1]
    c.execute('''INSERT INTO Funcs VALUES ('{0}', {1}, '⟨{2}⟩')'''.format(func.__name__, t, order))
connection.commit()
queries = []
queries.append(tuple([i for i in c.execute('''SELECT Name, min(Time) FROM Funcs''')]))
queries.append(tuple([i for i in c.execute('''SELECT Name, Time/(SELECT min(Time) FROM Funcs) FROM Funcs''')]))
queries.append(tuple([i for i in c.execute('''SELECT Name, Result FROM Funcs''')]))
for i,q in enumerate(queries):
    if i == 0:
        print("times as compared to the quickest: ", end="")
        print(q[0][0] + ": {:e}s".format(q[0][1]))
    for each in q:
        print(each)
    print()
connection.close()

# times = []
# start = time.time()
# q = quick(xlst)
# stop = time.time()
# times += [stop - start]
# b = bubble(xlst)
# print(q == b)
# stop2 = time.time()
# times += [stop2 - stop]
# print("\n")
# print("total run time:\n\nquicksort: {}\nbubble: {}\n~  ~ ~~  ~~ ~  ~\n".format(times[0],times[1]))
# scaled = [times[i]/min(times) for i in range(len(times))]
# print("proportional time:\n\nquicksort: {}\nbubble: {}\n~  ~ ~~  ~~ ~  ~\n".format(scaled[0],scaled[1]))

# print(quick(xlst))
# print(insertion(xlst)[0])
# print(bubble(xlst)[0])
# print(len(bubble(xlst)))
# import sqlite3

connection = sqlite3.connect("thisone.db")
c = connection.cursor()
c.execute("DROP TABLE IF EXISTS Placement")
c.execute("""CREATE TABLE Placement (Name text, Strategic real, Entertainment real)""")
c.execute("""INSERT INTO Placement VALUES ('Jenna Morasca', 8, 8)""")
c.execute("""INSERT INTO Placement VALUES ('Richard Hatch', 4, 7)""")
connection.commit()


def exeprint(string):
    print("*"*30)
    print(string.replace("\n",""))
    print()
    query = c.execute(string)
    for each in query:
        print(each)

exeprint("""SELECT * FROM Placement""")
exeprint("""SELECT *,(Strategic + Entertainment)/8 FROM Placement ORDER BY (Strategic + Entertainment) ASC""")

connection.close()