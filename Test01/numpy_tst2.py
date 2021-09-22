# Numpy_Tst2.py  Last updated:   21_08_11

import numpy as np

def func2(row, col):
    return 2 * row + col

print(__name__)

b = np.array([10,11, 12, 13])
# c = np.array([20,21, 22, 23])
c = np.arange(20, 24, 1)
print(f" c = { c } \n")
d = b + c
print(f" d = { d } \n")

e = b * 10
f = b * c
print(f" e = { e } ")
print(f" f = { f } \n")


g = np.sin(b)
     # .exp
	 # .log
print(f" g = { g } \n")


a = np.array([1, 2, 3])
print(f" a = { a }")
h = a + np.array([4])
print(f" h ={ h }\n")

k = a + np.array([5, 6, 7])
print(f" k = { k }")

m = []
for i in range(5):
   m.append(i)
print(f" m = { m }")

n = [(i+1) for i in range(5) ]
print(f"n = { n }")

#p = n**2   Not work
#print(f"p={ p }")

dot = 0
for i, j in zip(a,k):
     dot += i * j
print(f" dot(a,k)-for={ dot }")

dot2 = np.dot(a,k)
print(f" dot(a,k) = { dot2 }")

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
C = A * B     # elementwise product                           
print(f" C = A * B = { C }\n")   #  C = A * B = [[2 0]
                                 #               [0 4]]

M = A @ B     # matrix product
print(f" M = A @ B = { M }\n")   #  M = A @ B = [[5 4]
                                 #               [3 4]]

D = A.dot(B)  # another matrix product
print(f" D = A.dot(B) = { D }\n")   # D = A.dot(B) = [[5 4]
                                    #                 [3 4]]

S = B.sum(axis=0)     # sum of each column
print(f" B.sum(axis=0) = { S }\n")   # B.sum(axis=0) = [5 4]

M = B.min(axis=1)     # min of each row
print(f" B.min(axis=1) = { M }\n")   #  B.min(axis=1) = [0 3]

C = B.cumsum(axis=1)  # cumulative sum along each row
print(f" B.cumsum(axis=1) = { C }\n")   #  B.cumsum(axis=1) = [[2 2]
                                        #                      [3 7]]                         


r = np.fromfunction(func2, (5, 4), dtype=int)
print(f" np.fromfunction(func2, (5, 4)({ r } \n")  # func2(row, col) = 2 * row + col
   # np.fromfunction(func2, (5, 4)([[ 0  1  2  3]
   # [ 2  3  4  5]
   # [ 4  5  6  7]
   # [ 6  7  8  9]
   # [ 8  9 10 11]]

