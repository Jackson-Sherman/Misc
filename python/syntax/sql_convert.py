import sqlite3

class sql:
    def __init__(self,select_statement):
        self.rows = []
        if isinstance(select_statement, sqlite3.Cursor):
            self.rows = [list(row) for row in select_statement]
        self.r2 = None

    def setround(self, Round):
        assert isinstance(Round, int), "parameter must be type int"
        assert 0 <> Round, "parameter must be non-zero"
        assert 0 <= Round, "parameter must be positive"
        self.r2 = Round

    def getround(self):
        return self.r2

    def getrows(self):
        return self.rows

    def __str__(self):
        if not self.rows[0]:
            return ""
        widths = [0 for i in self.rows[0]]
        for row in self.rows:
            for i in range(len(row)):
                val = row[i]
                if self.getround():
                    l = 0
                    if isinstance(val, int):
                        l = len("{0:+}".format(val))
                    if isinstance(val, float):
                        st = ("{0:+." + self.getround() + "f}").format(val)
                        if "." + "0"*self.getround() in st:
                            l = len(str(int(val)))
                        else:
                            l = len(st)
                    else:
                        l = len(val)
                else:
                    if isinstance(val, int):
                        l = len(str(val))
                    if isinstance(val, float):
                    l = len(val)

                if l > widths[i]:
                    widths[i] = l
                
        
                    