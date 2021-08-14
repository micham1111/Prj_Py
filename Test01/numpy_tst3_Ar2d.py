# numpy_Tst3_Ar2d.py - Updated:   21_08_11  (20_04_20)

import numpy as np

print("Test numpy_Tst3_Ar2d:")

print(__name__)

e = np.array([[1,2,3,4,],[10,11, 12, 13]])
print(f"e = {e}")
    #[[ 1  2  3  4]
    # [10 11 12 13]]
print(f"e.ndim = {e.ndim}")

print(f"e.shape = {e.shape}")
        # (2, 4)	row major
print(f"e.size = {e.size}")
        # 8
print(f"e.nbytes = {e.nbytes}")
        # 32
print(f"e[0] = {e[0]}")
print(f"e[1,2] = {e[1,2]}")
     # 1
print()

print("e elements:")
for a in e:
     print(a)     
print()

print("e elements (op2):")
l = [print(a) for a in e]
print(l)          
print()



s = np.squeeze(e)
print(f"s = {s}")
print(f"s.ndim = {s.ndim}")
print(f"s.shape = {s.shape}")
print(f"np.squeeze(e).shape = {np.squeeze(e).shape}")


#s0 = np.squeeze(e, axis=0)
#print(f"s0.ndim = {s0.ndim}")
#print(f"s0.shape = {s0.shape}")

x = np.array([[[0], [1], [2]]])
print(f"x = {x}")
print(f"x.ndim = {x.ndim}")
print(f"x.shape = {x.shape}")

sx = np.squeeze(x)
print(f"sx = {sx}")
print(f"sx.ndim = {sx.ndim}")
print(f"sx.shape = {sx.shape}")

sx0 = np.squeeze(x, axis=0)
print(f"sx0 = {sx0}")
print(f"sx0.ndim = {sx0.ndim}")
print(f"sx0.shape = {sx0.shape}")

#sx1 = np.squeeze(x, axis=1) - error
sx2 = np.squeeze(x, axis=2)
print(f"sx2 = {sx2}")
print(f"sx2.ndim = {sx2.ndim}")
print(f"sx2.shape = {sx2.shape}")


#x.reshape(,-1)


a = np.array([[1,2], [3,4]])
print(f"a = {a}")

stmp = np.trace(a)
print(f"np.trace(a) = { stmp }")



