

import numpy as np

print(__name__)

print(f"numpy version = {np.__version__}")

a = np.arange(12)
print(f"a = {a}")
#   [ 0  1  2  3  4  5  6  7  8  9 10 11]

print(f"type(a) = {type(a)}")
   # numpy.ndarray

print(f"a.dtype = {a.dtype}")
    # dtype('int32')

print(f"a.ndim = {a.ndim}")
    # 1

print(f"a.itemsize = { a.itemsize }\n")
     #4

print(f"a.shape = {a.shape}\n")
   #	(12,)


r = a[1:4]
print(f"r = {r}\n")
    #  [1 2 3]

s = a[4:-2]
print(f"s = {s}\n")
# [4 5 6 7 8 9]

#grab first 3 elements
t = a[:3]
print(f"t = {t}\n")
# [0 1 2]

#grab last 2 elements 
w = a[-2:]
   # [10 11]
print(f"w = {w}\n")

z = a[::2]
   #[ 0  2  4  6  8 10]   step of 2
print(f"z = {z}\n")

#af = a.astype(np.float32)
af = a.astype('<f4')
print(f"af.dtype = { af.dtype }")
print(f"af.itemsize = { af.itemsize }")
       #4
print(f"af = { af }\n")

ad = a.astype('float')
print(f"ad.dtype = { ad.dtype }")
print(f"ad.itemsize = { ad.itemsize }")
      #8
print(f"ad = { ad }\n")


a = a.reshape(3,4)
print(f"a = {a}\n")
#  [[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

for c in a.flatten():
  print(c)
print()

# M:/Doc_Bk/OpenCV/learning-opencv-computer-vision-python-3rd_Howse20/learning-opencv-computer-vision-python-3rd.pdf
z = np.zeros((3, 3), dtype=np.uint8)
print(z)

