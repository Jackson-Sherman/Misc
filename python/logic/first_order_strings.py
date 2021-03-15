import re
from python.logic.testing import Logic

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
    {'proof', 'valid', 'bug', 'set'},
    {'proof', 'valid', 'logic', 'set', 'not'},
    {'proof', 'valid', 'logic', 'pun', 'not'},
    {'proof', 'valid', 'logic', 'set', 'program'},
    {'proof', 'valid', 'logic', 'not', 'program'},
    {'proof', 'logic', 'not', 'program'}
)

def prep(s):
    assert isinstance(s,str)
    return s.lower()

def r(s):
    return Logic(prep(s)[0] == "r")

def t(s):
    return Logic(prep(s)[0] == "t")

def f(s):
    return Logic(len(prep(s)) == 5)

def l(x,y):
    return Logic(len(prep(x)) > len(prep(y)))

def s(x,y):
    def shelp(a,b):
        assert isinstance(a,set)
        if len(a) == 0:
            return False
        
        c = a.pop()

        if c in b: return True

        else: return shelp(a,b)

    return Logic(shelp(set(prep(x)),set(prep(y))))

class Quant:
    '''A static class for quantifiers'''

    def __init__(self):
        pass

    def Ex(fun, gx):
        if len(gx) == 0: return False
        elif fun(gx.pop()): return True
        else: return Quant.Ex(fun,gx)

    def Ax(fun, gx):
        if len(gx) == 0: return True
        elif not fun(gx.pop()): return False
        else: return Quant.Ax(fun,gx)

    def ExEy(fun, gx):
        if len(gx) == 0: return False
        word = gx.pop()
        if Quant.Ex((lambda t: fun(t,word)), gx | {word}): return True
        else: return Quant.ExEy(fun,gx)

    def ExAy(fun, gx):
        if len(gx) == 0: return True
        word = gx.pop()
        if Quant.Ex((lambda t: fun(t,word)), gx | {word}): return False
        else: return Quant.ExAy(fun,gx)

    def AxEy(fun, gx):
        if len(gx) == 0: return False
        word = gx.pop()
        if Quant.Ax((lambda t: fun(t,word)), gx | {word}): return True
        else: return Quant.AxEy(fun,gx)

    def AxAy(fun, gx):
        if len(gx) == 0: return True
        word = gx.pop()
        if Quant.Ax((lambda t: fun(t,word)), gx | {word}): return False
        else: return Quant.AxAy(fun,gx)




    def Exn(fun, gx): return Quant.Ex((lambda x: not fun(x)), gx)

    def Axn(fun, gx): return Quant.Ax((lambda x: not fun(x)), gx)


    def nEx(fun, gx): return Quant.Axn(fun, gx)

    def nAx(fun, gx): return Quant.Exn(fun, gx)


    def nExn(fun, gx): return Quant.Ax(fun, gx)

    def nAxn(fun, gx): return Quant.Ex(fun, gx)



    def ExEyn(fun, gx): return Quant.ExEy((lambda x, y: not fun(x, y)), gx)

    def ExAyn(fun, gx): return Quant.ExAy((lambda x, y: not fun(x, y)), gx)

    def AxEyn(fun, gx): return Quant.AxEy((lambda x, y: not fun(x, y)), gx)

    def AxAyn(fun, gx): return Quant.AxAy((lambda x, y: not fun(x, y)), gx)


    def ExnEy(fun, gx): return Quant.ExAyn(fun, gx)

    def ExnAy(fun, gx): return Quant.ExEyn(fun, gx)

    def AxnEy(fun, gx): return Quant.AxAyn(fun, gx)

    def AxnAy(fun, gx): return Quant.AxEyn(fun, gx)


    def ExnEyn(fun, gx): return Quant.ExAy(fun, gx)

    def ExnAyn(fun, gx): return Quant.ExEy(fun, gx)

    def AxnEyn(fun, gx): return Quant.AxAy(fun, gx)

    def AxnAyn(fun, gx): return Quant.AxEy(fun, gx)


    def nExEy(fun, gx): return Quant.AxnEy(fun, gx)

    def nExAy(fun, gx): return Quant.AxnAy(fun, gx)

    def nAxEy(fun, gx): return Quant.ExnEy(fun, gx)

    def nAxAy(fun, gx): return Quant.ExnAy(fun, gx)


    def nExEyn(fun, gx): return Quant.AxnEyn(fun, gx)

    def nExAyn(fun, gx): return Quant.AxnAyn(fun, gx)

    def nAxEyn(fun, gx): return Quant.ExnEyn(fun, gx)

    def nAxAyn(fun, gx): return Quant.ExnAyn(fun, gx)


    def nExnEy(fun, gx): return Quant.AxEy(fun, gx)

    def nExnAy(fun, gx): return Quant.AxAy(fun, gx)

    def nAxnEy(fun, gx): return Quant.ExEy(fun, gx)

    def nAxnAy(fun, gx): return Quant.ExAy(fun, gx)


    def nExnEyn(fun, gx): return Quant.AxEyn(fun, gx)

    def nExnAyn(fun, gx): return Quant.AxAyn(fun, gx)

    def nAxnEyn(fun, gx): return Quant.ExEyn(fun, gx)

    def nAxnAyn(fun, gx): return Quant.ExAyn(fun, gx)

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

quan = parseForNot(input("    quantifier: ")) # raw input of quantifier

cnt = quan.count("A") + quan.count("E")

lambstring = "lambda x" + ("" if cnt < 2 else ", y") + ": " # developing the head of a lambda to be eval'ed later
funstring = input("type the function: " + dis(quan) + " ") # the raw function
inpfun = eval(lambstring + "bool(" + funstring + ")")
finalfun = lambda setalgo: Quant.__dict__[quan](inpfun, setalgo)
print()
print(disp(quan) + "(" + funstring + ")" * cnt)
print()
for i,j in enumerate(models):
    print("   M{}: {}".format(i+1,finalfun(j)))
print()