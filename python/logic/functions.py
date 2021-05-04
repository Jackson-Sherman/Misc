

class Function:
    def integer(n=1000):
        return

    def natural(n=1000):
        return
    
    def __init__(self, domain=set(), dom_fun=(lambda x: False), codomain=set(), cod_fun=(lambda x: False), relation_dict={}, function=(lambda a: None)):
        if domain:
            self.dom = lambda x: x in domain
            
        else:
            self.dom = dom_fun

        if codomain:
            self.cod = lambda x: x in codomain

        else:
            self.cod = cod_fun
            

        if relation_dict:
            self.fun = lambda x: relation_dict[x]

        else:
            self.fun = function
    
    def one_to_one(self):
        outputs = set()
        for a in self.dom:
            val = self.fun(a)
            assert val in self.cod

            if val in outputs:
                return val
            else:
                outputs |= {val}
        
        return None
    
    def onto(self):
        outputs = set()

        for each in self.dom:
            val = self.fun(each)
            assert val in self.cod
            outputs |= {val}
        
        dif = self.cod - outputs
        return dif

    def __str__(self):
        output = '  onto: '
        onto = self.onto()
        output += 'yes' if onto == set() else 'no ' + str(onto)
        output += '\n'
        output += '1 to 1: '
        one_to_one = self.one_to_one()
        output += 'yes' if one_to_one is None else 'no ' + str(one_to_one)
        return output

if __name__ == '__main__':
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    A = {1,2,3}
    B = {a,b,c,d}
    hw11_1 = Function(A,B,{1:a,2:b,3:c})
    print(hw11_1)