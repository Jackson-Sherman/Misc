import math
class Base:
    s2n = {}
    n2s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    for i,j in enumerate(n2s):
        s2n[j] = i
    def __init__(self, value, base):
        assert base < 65, 'Base too large, sorry :('
        self.base = base
        value = str(value)
        self.l = len(value)
        if '.' in value:
            i = value.index('.')
            self.v = value[:i]+value[i+1:]
            self.d = i
            self.l -= 1
        else:
            self.v = value
            self.d = self.l

    def __add__(self,other):
        sd, sl, sv = self.d, self.l, self.v
        od, ol, ov = other.d, other.l, other.v
        while sd < od:
            sd += 1
            sl += 1
            sv = '0' + sv
        while od < sd:
            od += 1
            ol += 1
            ov = '0' + ov
        while sl < ol:
            sl += 1
            sv += '0'
        while ol < sl:
            ol += 1
            ov += '0'
        ol,od,sl,sd = ol+1,od+1,sl+1,sd+1
        ov = '0' + ov
        sv = '0' + sv

        def adding(x,y,l,c=False):
            if 0 < l:
                val = self.s2n[x[l-1]]+ self.s2n[y[l-1]] + (1 if c else 0)
                new_c = False
                if val >= self.base:
                    val -= self.base
                    new_c = True
                return adding(x,y,l-1,new_c) + self.n2s[val]
            else:
                return ''
        
        kv = adding(sv,ov,sl)
        kd = sd
        kl = sl

        while kv[0] == '0':
            kv = kv[1:]
            kl -= 1
            kd -= 1
        while kv[kl-1] == '0':
            kv = kv[:-1]
            kl -= 1
        if kd < kl:
            kv = kv[:d] + '.' + kv[d:]
        return Base(kv, self.base)

    def __str__(self):
        return self.v[:self.d] + ('.' if self.d < self.l else '') + self.v[self.d:] + '_' + str(self.base)


if __name__ == "__main__":
    x = Base(15,6)
    y = Base(44,6)
    z = x+y
    print(z)