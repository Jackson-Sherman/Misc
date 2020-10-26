import random
import time
xlst = [int(random.random()*90)+10 for i in range(4)]

def insertion(lst):
    if len(lst) < 2:
        return lst
    else:
        mini = min(lst)
        lst.remove(mini)
        return [mini] + insertion(lst)

def bubble(lst):
    def flip(ind,jnd):
        """
        inde
        """
        algoi = lst[ind]
        algoj = lst[jnd]
        lst[ind] = algoj
        lst[jnd] = algoi
    
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                algoi = lst[i]
                algoj = lst[j]
                lst[i] = algoj
                lst[j] = algoi
    return lst


def quick(lst):
    if len(lst) <= 1:
        return lst
    else:
        # check = lst[0]
        # before = []
        # after = []
        def beforeAndAfter(check,xlst,b=[],a=[]):
            if xlst:
                if xlst[0] <= check:
                    return beforeAndAfter(check, xlst[1:], b+[xlst[0]], a)
                else:
                    return beforeAndAfter(check, xlst[1:], b, a+[xlst[0]])
            else:
                return b + [check] + a
        c = xlst[0]
        return quick(beforeAndAfter(c,xlst))
        # for i in range(1,len(lst)):
        #     if lst[i] <= check:
        #         before += [lst[i]]
        #     else:
        #         after += [lst[i]]
        # return quick(before) + [check] + quick(after)

print(xlst)
print("")
times = []
start = time.time()
q = quick(xlst)
stop = time.time()
times += [stop - start]
b = bubble(xlst)
print(q == b)
stop2 = time.time()
times += [stop2 - stop]
print("\n")
print("total run time:\n\nquicksort: {}\nbubble: {}\n~  ~ ~~  ~~ ~  ~\n".format(times[0],times[1]))
scaled = [times[i]/min(times) for i in range(len(times))]
print("proportional time:\n\nquicksort: {}\nbubble: {}\n~  ~ ~~  ~~ ~  ~\n".format(scaled[0],scaled[1]))

print(quick(xlst))
print(insertion(xlst)[0])
print(bubble(xlst)[0])
print(len(bubble(xlst)))