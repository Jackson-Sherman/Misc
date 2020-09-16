
#INPUT: all are floats where 0 <= input < 1
#INPUT: h=hue, s=saturation, v=value
def hsv_to_rgb(h, s, v):

    def zero_to_one(x):
        if x < 0:
            return 0

        elif 1 < x:
            return 1

        else:
            return x
    


    h = zero_to_one(h)
    s = zero_to_one(s)
    v = zero_to_one(v)

    if v == 0:
        return (0, 0, 0)
    
    def setting_hue(hue):
        ok = hue * 6
        col = []

        if ok < 1:
            ok %= 1
            col = [1, ok, 0]

        elif ok < 2:
            ok %= 1
            col = [1-ok, 1, 0]

        elif ok < 3:
            ok %= 1
            col = [0, 1, ok]

        elif ok < 4:
            ok %= 1
            col = [0, 1-ok, 1]

        elif ok < 5:
            ok %= 1
            col = [ok, 0, 1]

        else:
            ok %= 1
            col = [1, 0, 1-ok]
        
        return col
    
    the_color = setting_hue(h)

    def scaling(RGorB):
        mini = v - (s * v)
        maxi = v
        out = (maxi - mini) * RGorB + mini
        out = s*v * RGorB - s*v + v 
        return out

    for x in (0,1,2):
        the_color[x] = scaling(the_color[x])
        the_color[x] = int(256 * the_color[x]) if the_color[x] < 1 else 255

    return tuple(the_color)