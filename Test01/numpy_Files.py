import numpy

print(__name__)
print(__doc__)

# Read raw data from a binary file
PathR = r'W:\Image_db\Patterns\Inc0_16x16.f32' # r' for read text without special chars
with open(PathR, 'rb') as f: # with is context manager, it closed the file in the end of the scope
    data = numpy.fromfile(f, '<f4') # little-endian float32

print('Type Data: ', type(data))    
print('Data Shape: ', data.shape)    
print('Data ndim: ', data.ndim)    
print('Data Size: ', data.size)  
print('Data sum: ', data.sum())     
print('Data min: ', data.min())     
print('Data mean: ', data.mean())     
print('Data std: ', data.std())     
print()

#def Read_File(FilePath):
#    with open(FilePath, 'rb') as f: # with is context manager, it closed the file in the end of the scope
#        data = numpy.fromfile(f, '<f4') # littclle-endian float32    
#        return data

#path = r'W:\Image_db\Patterns\Inc0_16x16.f32' # r' for read text without special chars
#data = Read_File(path)

#VecInc2_257_256x1.f32

# Read raw data from a binary file
def Read_File(path):
    dat = []
    with open(path, 'rb') as f: # with is context manager, it closed the file in the end of the scope
        dat = numpy.fromfile(f, '<f4') # little-endian float32
    return dat

dataF = Read_File(PathR)
print("dataF:")
print(dataF)



PathW = r'W:\TempW\Temp0_16x16.f32' # r' for read text without special chars

# Write raw data to a binary file
def Write_File(path, dat):
    with open(path, 'wb') as f: # with is context manager, it closed the file in the end of the scope
        dat.tofile(f, '<f4') # little-endian float32

Write_File(PathW, dataF)


def Write_File1(path, dat):
    fileobj = open(path, mode='wb')
    dat.tofile(fileobj)
    fileobj.close()

PathW1 = r'W:\TempW\Temp0_16x16.i32'

nparI = numpy.array([1, 256], dtype=numpy.int32)
print(nparI)
Write_File1(PathW1, nparI)

