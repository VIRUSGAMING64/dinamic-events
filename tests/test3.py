#para hacer test a segtree

from modules import SegTree
from random import *
a = []
mx = 0
for i in range(10**5):
    b=randint(1,10**9)
    a.append(b)
    mx = max(mx,b)


tree = SegTree(a)


o = tree.query(0,len(a) - 1)

print(mx , o)

assert mx == o