import re
from c241 import Logic

def collect():
    seto = set()
    print()
    string = input("enter a string to be added: ")
    while string:
        print()
        seto |= {string}
        string = input("enter a string to be added: ")
    print()
    print("The set: " + str(seto))

print()

models = (
    (1,3,4,6),
    (2,4,5,7),
    (1,2,3,4),
    (2,3,4,5),
    (1,2,3,4,5),
)
fullset = set()
for row in models:
    fullset |= set(row)

def o(n):
    return Logic(int(n)%2==1)

def e(n):
    return Logic(int(n)%2==0)

def b(x,y):
    return Logic(x > y)

# def drawing(fun,mods,two=True):
#     vals = ((),())
#     for i in mods:
#         if two:
#             v = fun(i)
#             if v: vals = vals[0] + ((i,v),), vals[1]
#             else: vals = vals[0], vals[1] + ((i,v),)
#         else:
#             for j in mods:
#                 if i == j or two:
#                     v = fun(i,j)
#                     if v: vals = vals[0] + (((i,j),v),), vals[1]
#                     else: vals = vals[0], vals[1] + (((i,j),v),)

#     for tf in vals:
#         for each in tf:
#             if two:
#                 print(('{}({:<7}' + ', {:<7}' if two else ''  + ') = {}').format(fun.__name__,*each[0][0 if two else 1:],each[1]))
#             else:
#                 print()

# drawing(f,fullset,False)

class Quant:
    '''A static class for quantifiers'''

    def __init__(self):
        pass

    def Ex(fun, gx): return True in [bool(fun(word)) for word in gx]

    def Ax(fun, gx): return False not in [bool(fun(word)) for word in gx]

    def ExEy(fun, gx): return True in [True in [bool(fun(i,j)) for i in gx] for j in gx]
        # if len(gx) == 0: return False
        # word = gx.pop()
        # gx.add(word)
        # if Quant.Ex((lambda t: fun(t,word)), gx): return True
        # return Quant.ExEy(fun, gx - {word})

    def ExAy(fun, gx): return True in [False not in [bool(fun(i,j)) for i in gx] for j in gx]
        # if len(gx) == 0: return True
        # word = gx.pop()
        # gx.add(word)
        # if Quant.Ex((lambda t: fun(t,word)), gx): return False
        # return Quant.ExAy(fun, gx - {word})

    def AxEy(fun, gx): return False not in [True in [bool(fun(i,j)) for i in gx] for j in gx]
        # if len(gx) == 0: return False
        # word = gx.pop()
        # gx.add(word)
        # if Quant.Ax((lambda t: fun(t,word)), gx): return True
        # return Quant.AxEy(fun, gx - {word})

    def AxAy(fun, gx): return False not in [False not in [bool(fun(i,j)) for i in gx] for j in gx]
        # if len(gx) == 0: return True
        # word = gx.pop()
        # gx.add(word)
        # if Quant.Ax((lambda t: fun(t,word)), gx): return False
        # return Quant.AxAy(fun, gx - {word})




    def Exn(fun, gx): return Quant.Ex((lambda x: not fun(x)), gx)

    def Axn(fun, gx): return Quant.Ax((lambda x: not fun(x)), gx)


    def nEx(fun, gx): return not Quant.Ex(fun, gx)

    def nAx(fun, gx): return not Quant.Ax(fun, gx)


    def nExn(fun, gx): return not Quant.Ex((lambda x: not fun(x)), gx)

    def nAxn(fun, gx): return not Quant.Ax((lambda x: not fun(x)), gx)



    def ExEyn(fun, gx): return Quant.ExEy((lambda x, y: not fun(x, y)), gx)

    def ExAyn(fun, gx): return Quant.ExAy((lambda x, y: not fun(x, y)), gx)

    def AxEyn(fun, gx): return Quant.AxEy((lambda x, y: not fun(x, y)), gx)

    def AxAyn(fun, gx): return Quant.AxAy((lambda x, y: not fun(x, y)), gx)


    def ExnEy(fun, gx): return Quant.ExAy((lambda x, y: not fun(x, y)), gx)

    def ExnAy(fun, gx): return Quant.ExEy((lambda x, y: not fun(x, y)), gx)

    def AxnEy(fun, gx): return Quant.AxAy((lambda x, y: not fun(x, y)), gx)

    def AxnAy(fun, gx): return Quant.AxEy((lambda x, y: not fun(x, y)), gx)


    def ExnEyn(fun, gx): return Quant.ExAy(fun, gx)

    def ExnAyn(fun, gx): return Quant.ExEy(fun, gx)

    def AxnEyn(fun, gx): return Quant.AxAy(fun, gx)

    def AxnAyn(fun, gx): return Quant.AxEy(fun, gx)


    def nExEy(fun, gx): return not Quant.ExEy(fun, gx)

    def nExAy(fun, gx): return not Quant.ExAy(fun, gx)

    def nAxEy(fun, gx): return not Quant.AxEy(fun, gx)

    def nAxAy(fun, gx): return not Quant.AxAy(fun, gx)


    def nExEyn(fun, gx): return not Quant.ExEy((lambda x, y: not fun(x, y)), gx)

    def nExAyn(fun, gx): return not Quant.ExAy((lambda x, y: not fun(x, y)), gx)

    def nAxEyn(fun, gx): return not Quant.AxEy((lambda x, y: not fun(x, y)), gx)

    def nAxAyn(fun, gx): return not Quant.AxAy((lambda x, y: not fun(x, y)), gx)


    def nExnEy(fun, gx): return not Quant.ExnEy(fun, gx)

    def nExnAy(fun, gx): return not Quant.ExnAy(fun, gx)

    def nAxnEy(fun, gx): return not Quant.AxnEy(fun, gx)

    def nAxnAy(fun, gx): return not Quant.AxnAy(fun, gx)


    def nExnEyn(fun, gx): return not Quant.ExnEy((lambda x, y: not fun(x, y)), gx)

    def nExnAyn(fun, gx): return not Quant.ExnAy((lambda x, y: not fun(x, y)), gx)

    def nAxnEyn(fun, gx): return not Quant.AxnEy((lambda x, y: not fun(x, y)), gx)

    def nAxnAyn(fun, gx): return not Quant.AxnAy((lambda x, y: not fun(x, y)), gx)

replaces = lambda s, t: s if len(t) == 0 else replaces(s.replace(t[0][0],t[0][1]), t[1:])

delete = lambda s, c: s[:s.find(*c)] + s[s.find(*c)+1:]

dis = lambda s: replaces(s, [('n','¬')])

disp = lambda s: delete(replaces(s, [('n','¬'), ('A', '(A'), ('E', '(E')]), ['('])

def parseForNot(q):
    assert isinstance(q,str)
    q = q.replace(' ','')
    q = q.replace('not','n')
    q = q.replace('-','n')
    q = q.replace('~','n')
    q = q.replace('nn','')
    assert q in Quant.__dict__
    return q

def loop():
    print()
    quantifier_input = input("*"*31+"\n\n    quantifier: ") # raw input of quantifier
    if quantifier_input:
        print()
        quan = parseForNot(quantifier_input) 

        cnt = quan.count("A") + quan.count("E")

        lambstring = "lambda x" + ("" if cnt < 2 else ", y") + ": " # developing the head of a lambda to be eval'ed later
        funstring = input("    function: " + dis(quan) + " ") # the raw function
        inpfun = eval(lambstring + "bool(" + funstring + ")")
        finalfun = lambda setalgo: Quant.__dict__[quan](inpfun, setalgo)
        print()
        print(disp(quan) + "(" + funstring + ")" * cnt)
        print()
        for i,j in enumerate(models): print("   M{}: {}\t{}".format(i+1, finalfun(set(j)), j))
        loop()

if __name__ == '__main__': loop()
