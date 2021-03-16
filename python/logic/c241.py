class Logic:
    def __init__(self,value):
        if value:
            if isinstance(value,str):
                if "T" in value.upper():
                    self.value == True
                elif "F" in value.upper():
                    self.value == False
                else:
                    try:
                        self.value = bool(float(value))
                    except:
                        self.value = bool(value)
            else:
                self.value = bool(value)
        else:
            self.value = False

    def __bool__(self):
        return self.value
    
    def __or__(self, other):
        return Logic(bool(self) or bool(other))
    
    def __add__(self, other):
        return self | other
    
    def __radd__(self, other):
        return self + other

    def __xor__(self, other):
        return Logic(not bool(self == other))
    
    def __mod__(self, other):
        return self ^ other
    
    def __and__(self, other):
        return Logic(bool(self) and bool(other))

    def __mul__(self, other):
        return self & other
    
    def __rmul__(self, other):
        return self & other
    
    def __neg__(self):
        return Logic(not bool(self))
    
    def __invert__(self):
        return self.__neg__()
    
    def __eq__(self, other):
        return Logic(bool(self) and bool(other) or not bool(self) and not bool(other))

    def __gt__(self, other):
        return Logic(not bool(self) or bool(other))

    def __str__(self):
        return "O" if self.value else "X"
    
    def __format__(self, format_spec):
        return str(self).__format__(format_spec)

class Formatted:
    '''
    A class to format strings to print them with big parenthesis
    '''
    typeof = {
        '(':'p',
        ')':'p',
        '[':'s',
        ']':'s',
        '{':'c',
        '}':'c',
    }

    openbrac = {
        '(':'p',
        '[':'s',
        '{':'c'
    }

    closebrac = {
        ')':'p',
        ']':'s',
        '}':'c'
    }

    def __init__(self, string):
        self.string = string

    def parser(self):
        stack = []
        for i, char in enumerate(self.string):
            pass
