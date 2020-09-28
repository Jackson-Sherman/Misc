def b():
    breakstring = "    ~   ~~  ~~~ ~~~~ ~~~  ~~   ~    "
    print(breakstring)

def f():
    for i in range(0,6):
        print((" " * (i + 15) + "{}").format(i))

def w():
    i = 0
    while i < 6:
        print((" " * (i + 15) + "{}").format(i))
        i += 1

def r():
    def loop(n):
        if n < 6:
            print((" " * (n + 15) + "{}").format(n))
            loop(n + 1)
        else:
            pass
    i = 0
    loop(i)


b()
f()
b()
w()
b()
r()
b()