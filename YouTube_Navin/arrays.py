from array import *
from numpy import *

baba = array('i', [ 1, 2, 3, -3 ])
print(baba)
baba.reverse()
print(baba.buffer_info())
print(baba)
print(baba.typecode)

for i in baba:
    print(i)

print()
print()

for i in range(4):
    print(baba [ i ])

print()
print()

for i in range(len(baba)):
    print(baba [ i ])

print()
print()

newArray = array(baba.typecode, (a*3 for a in baba))
print(newArray)

for k in newArray:
    print(k, end=" ")


