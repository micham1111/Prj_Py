import numpy

print(__name__)
print(__doc__)

# Read raw data from a binary file
PathR = r'W:\Image_db\Patterns\Inc0_16x16.f32' # r' for read text without special chars
PathW = r'W:\TempW\Temp0_16x16.f32' # r' for read text without special chars

# Read raw data from a binary file
def Read_File(path):
    dat = []
    with open(path, 'rb') as f: # with is context manager, it closed the file in the end of the scope
        dat = numpy.fromfile(f, '<f4') # little-endian float32
    return dat

# Write raw data to a binary file
def Write_File(path, dat):
    with open(path, 'wb') as f: # with is context manager, it closed the file in the end of the scope
        dat.tofile(f, format='<f4') # little-endian float32

dataF = Read_File(PathR)
Write_File(PathW, dataF)
dataF2 = Read_File(PathW)
