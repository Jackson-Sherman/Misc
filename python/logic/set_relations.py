import networkx as nx
import matplotlib.pyplot as plt

class RelationMatrix:
    class Output:
        def __init__(self, value, counter_example=None):
            self._value = value
            self._counter_example = counter_example
        
        def __str__(self):
            output = "Yes!" if self._value else "No"
            
            if self._counter_example is None:
                return output

            return output + " - " + str(self._counter_example)

        def getValue(self):
            return self._value

        def getCounterExample(self):
            return self._counter_example



    def __init__(self, relset=set(), relation=lambda x,y: False, domain=[], range_=[], name=""):
        self.dom = set(domain)
        self.ran = set(range_)
        if len(self.dom)*len(self.ran) == 0:
            if len(self.ran) < len(self.dom):
                self.ran = self.dom
            
            else:
                self.dom = self.ran
        
        self.rel = relset
        self.relation = relation
        self._name = name
        
        if len(self.dom) == 0 and len(self.ran) == 0 and 0 < len(self.rel):
            for a,b in self.rel:
                self.dom |= {a}
                self.ran |= {b}
        
        elif len(self.rel) == 0 and 0 < len(self.dom) and 0 < len(self.ran):
            for a in self.dom:
                for b in self.ran:
                    if self.relation(a,b):
                        self.rel |= {(a,b)}

    def setOfPairsToListOfSingles(inputSet):
        front = set()
        back = set()
        for inp, out in inputSet:
            front |= {inp}
            back |= {out}
        
        middle = front & back
        front = front - middle
        back = back - middle

        return list(front).sort() + list(middle).sort() + list(back).sort()
    
    def relates(self, a, b):
        return ((a,b) in self.rel) or self.relation(a,b)
        
    def __dict__(self):
        return {a: {b: 1 if self.relates(a,b) else 0 for b in self.ran} for a in self.dom}
    
    def draw(self):
        G = nx.DiGraph()
        G.add_edges_from(list(self.rel))

        self_pointing_nodes = set()
        for a,b in self.rel:
            if a == b:
                self_pointing_nodes |= {a}
        
        def unique(l, v=[]):
            if len(l) < 1:
                return v
            
            if l[0] in v:
                return unique(l[1:], v)
            
            return unique(l[1:], v + [l[0]])
        
        # width = 0
        # for a,b in self.rel:
        #     la,lb = len(str(a)), len(str(b))
        #     width = max(width, max(la, lb))

        # w = "{:>" + str(width) + "}"
        # for i,j in enumerate(self.rel):
        #     print(w.format(str(j)),end=('\n' if i%5 == 0 else ''))

        print(self.rel)

        pos = nx.planar_layout(G)
        nx.draw_networkx(G,pos)
        # nx.draw_networkx_nodes(G,pos,unique([i for i in self_pointing_nodes]),node_color='r')
        # nx.draw_networkx_nodes(G,pos,unique([i for i in (set(self.dom) - self_pointing_nodes)]))
        # nx.draw_networkx_edges(G,pos,unique(list(self.rel)),arrowstyle='-|>')
        # nx.draw_networkx_labels(G,pos,{e:e for e in self.dom if e in pos})
        plt.show()

    def toGraph(self):
        if self.rel != set():
            return nx.Graph(list(self))
        
        return nx.Graph(dict(self))
        

    def isReflexive(self, domain={}):
        d = set(domain if domain else self.dom)

        for a in d:
            if not self.relates(a,a):
                return RelationMatrix.Output(False, "({0},{0})∉{1}".format(a,self._name))
            
        return RelationMatrix.Output(True)

    def isAntiReflexive(self, domain={}):
        d = set(domain if domain else self.dom)

        for a in d:
            if self.relates(a,a):
                return RelationMatrix.Output(False, "({0},{0})∈{1}".format(a,self._name))

        return RelationMatrix.Output(True)

    def isSymmetric(self, domain={}):
        d = set(domain if domain else self.dom)

        for a in d:
            for b in d:
                if self.relates(a,b) and not self.relates(b,a):
                    return RelationMatrix.Output(False, "({0},{1})∈{2} but ({1},{0})∉{2}".format(a,b,self._name))

        return RelationMatrix.Output(True)

    def isAntiSymmetric(self, domain={}):
        d = set(domain if domain else self.dom)

        for a in d:
            for b in d:
                if self.relates(a,b) and self.relates(b,a) and a != b:
                    return RelationMatrix.Output(False, "({0},{1})∈{2} and ({1},{0})∈{2}".format(a,b,self._name))

        return RelationMatrix.Output(True)
    
    def isTransitive(self, domain={}):
        d = domain if domain else self.dom

        for a in d:
            for b in d:
                for c in d:
                    if self.relates(a,b) and self.relates(b,c):
                        if not self.relates(a,c):
                            return RelationMatrix.Output(False, "({0},{1})∈{3} and ({1},{2})∈{3} but ({0},{2})∉{3}".format(a,b,c,self._name))
        
        return RelationMatrix.Output(True)
    
    def __str__(self):
        output  = '\n     reflexive: ' + str(self.isReflexive())
        output += '\nanti-reflexive: ' + str(self.isAntiReflexive())
        output += '\n     symmetric: ' + str(self.isSymmetric())
        output += '\nanti-symmetric: ' + str(self.isAntiSymmetric())
        output += '\n    transitive: ' + str(self.isTransitive())
        return output + '\n'