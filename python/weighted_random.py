import math
import random



def select(xlst):
    total = 0
    for element in xlst:
        if not(type(5) == type(element) or type(5.3) == type(element)):
            print("data is not entirely numeric")
            break
        total += element

    print("total: {}".format(total))
    scaled = []

    for i,j in enumerate(xlst):
        scaled.append(j / total)

    total = 0

    for el in xlst:
        total += el
    
    print("new total: {}".format(total))
    print("")
    print(xlst)
    print(scaled)

test_list = [9,3,20,4,1]

select(test_list)