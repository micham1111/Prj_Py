# LibFiles.py Updated: 21_09_01   20_06_12
# numpy types
# https://docs.scipy.org/doc/numpy/user/basics.types.html 


import numpy
import io

# Read raw data from a binary file
def Read_File(path, data_type='<f4'):
    print(f" Read_File: {path} ")
    with open(path, 'rb') as f: # with is context manager, it closed the file in the end of the scope
        # dat = numpy.fromfile(f, '<f4') # little-endian float32
        dat = numpy.fromfile(f, data_type) 
    return dat

# Read raw data from a binary file
def Read_File2(path):
    print(f" Read_File: {path} ")
    dat = []
    with open(path, 'rb') as f: # with is context manager, it closed the file in the end of the scope
        dat = numpy.fromfile(f, '<f4') # little-endian float32
    return dat

# File => File.npy
def Write_FileNpy(path, data):
    print(f" Write_File: { path } ")
    numpy.save(path, data)

# work ok
def Write_File1(path, data):
    print(f" Write_File: { path } ")
    file = io.open(path, "wb")
    file.write(data)
    file.close()


def Write_File(path, data):
    print(f" Write_File: { path } ")
    data.tofile(path)



'''
import io
stream = io.open("sample.txt", "r")
print stream.read()

file = open("sample.bin", "wb")
file.write(b"This binary string will be written to sample.bin")
file.close()

a.tofile('test2.dat')
a2 = np.fromfile('test2.dat', dtype=int)


def Write_File(path, data):
    print(f" Write_File: { path } ")
    with open(path, 'wb') as f: # with is context manager, it closed the file in the end of the scope
         np.fromfile(f, '<f4') # little-endian float32
    return dat


Add functions:


CopyFile(SrcPath, DstPath, SrcOffsetX=0, SrcOffsetY=0, DstOffsetX=0, DstOffsetY=0, Data_Type='<f4')) Not needed

'''
