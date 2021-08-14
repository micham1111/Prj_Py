
# Numpy_Random_Tst.py  Last updated:   21_08_11

import numpy as np

print(__name__)

a = np.array([10,11, 12, 13])
print(f"a = {a}")
print(f"a.mean = {a.mean()}")

b = a < 12 
print(f"b = {b}")

a = a + 10
print(f"a = {a}")



rolls = np.random.randint(low=1, high=6, size=10)
print(f"rolls = {rolls}")

randint2_3 = np.random.randint(low=1, high=6, size=(2,3))
print(f"randint2_3 = {randint2_3}")

l = a.tolist()
print(f"l = {l}")

xlist = [[1,2,3],[2,4,6]]
#print(f"xlist[1,-1] = {xlist[1,-1]}")  Error

x = np.asarray(xlist)
print("xlist = {}\nx ={}".format(xlist, x))

print(f"x[1,-1] = {x[1,-1]}")

ran = np.random.random()
print(f"ran = { ran }\n")

ran2_3 = np.random.random((2, 3))
print(f"ran2_3 = { ran2_3 }\n")

randn2_3 = np.random.randn(2, 3)
print(f"randn2_3 = { randn2_3 }\n")

