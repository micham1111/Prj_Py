# Numpy_Tst2.py  Last updated:   21_08_11

import numpy as np

print(__name__)

b = np.array([10,11, 12, 13])
c = np.array([20,21, 22, 23])
d = b + c
print(d)
print()

e = b * 10
f = b * c
print(e)
print(f)
print()


g = np.sin(b)
     # .exp
	 # .log
print(g)


a = np.array([1, 2, 3])
print(f"a={ a }")
h = a + np.array([4])
print(f"h={ h }\n")

k = a + np.array([5, 6, 7])
print(f"k={ k }")

m = []
for i in range(5):
   m.append(i)
print(f"m={ m }")

n = [(i+1) for i in range(5) ]
print(f"n={ n }")

#p = n**2   Not work
#print(f"p={ p }")

dot = 0
for i, j in zip(a,k):
     dot += i * j
print(f"dot(a,k)for={ dot }")

dot2 = np.dot(a,k)
print(f"dot(a,k)={ dot2 }")