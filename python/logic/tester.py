from set_relations import RelationMatrix as rm
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# relations = (
#     rm(relset={
#         ('a','a'),('a','b'),('a','c'),('a','d'),
#         ('b','d'),
#         ('c','d'),
#         ('c','d'),
#         ('d','d')
#     }, domain=['a','b','c','d'], name='R'),
#     rm(relset={
#         (1,1),(1,2),(1,3),
#         (2,1),(2,2),(2,3),(2,4),
#         (3,1),(3,3)
#     }, domain=[1,2,3,4], name='S'),
#     rm(relation=(lambda x,y: abs(x + y) % 2 == 1), domain=list(range(0,6)), name='Q'),
#     rm(relation=(lambda x,y: x in y and x != y), domain=[
#         'a','b','c','ab','ba','ac','ca','bc','cb','abc','acb','cab','cba','bca','bac',
#         # 'd','ad','da','bd','db','cd','dc','abd','adb','dab','dba','bda','bad',
#         # 'adc','acd','cad','cda','dca','dac','dbc','dcb','cdb','cbd','bcd','bdc',
#         # 'abcd','acbd','cabd','cbad','bcad','bacd',
#         # 'abdc','acdb','cadb','cbda','bcda','badc',
#         # 'adbc','adcb','cdab','cdba','bdca','bdac',
#         # 'dabc','dacb','dcab','dcba','dbca','dbac'
#     ], name='C'),
#     rm(relation=lambda x,y: 2 * x > y, domain=[(-1 if i < 0 else 1) * abs(i) ** 0.5 for i in range(-10,10,3)], name='D'),
#     rm(relation=lambda x,y: 2 * x > y, domain=[ i for i in range(-10,11,1)], name='D'),
#     rm(relation=lambda x,y: x.count('X') > y.count('X'), domain=["1X","2XX","3XXX","4XXXX"], name='D'),
# )

rel = rm(relation=(lambda x,y: set(x) <= set(y)), domain=[
    'x','y','z',
    'xx','xy','xz','yx','yy','yz','zx','zy','zz',
    'xxx','xxy','xxz','xyx','xyy','xyz','xzx','xzy','xzz',
    'yxx','yxy','yxz','yyx','yyy','yyz','yzx','yzy','yzz',
    'zxx','zxy','zxz','zyx','zyy','zyz','zzx','zzy','zzz',
], name='B')
print(rel)
rel = rm(relation=(lambda x,y: y % x == 0), domain=list(range(1,30)), name='B')
print(rel)
print()
rel.draw()
print()
# G = nx.DiGraph()
# G.add_edges_from([(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,3),(2,4)])
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G,pos,[1,2,3,4])
# nx.draw_networkx_edges(G,pos,arrowstyle='-|>')
# nx.draw_networkx_labels(G,pos,{i:i for i in range(1,5)})
# plt.show()

# for relation in relations:
#     print(relation)