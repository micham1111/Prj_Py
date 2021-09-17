# Sys_Tst1.py  updated: 21_09_16  20_04_05
import sys
import builtins

print("Sys Test:")
print(f"__name__= { __name__ }")   # __name__= __main__
print(f"__doc__ = { __doc__}")     # __doc__ = None
print('sys.version = ', sys.version)          # sys.version =  3.7.4 ...
print('sys.executable = ', sys.executable)    # sys.executable = D:\Anaconda3\python.exe
print('sys.version_info[0] = ', sys.version_info[0])   # sys.version_info[0] = 3


# file:///M:/Doc_Bk/Python_ML/byte-of-python.pdf
# if os.system(zip_command) == 0:
#    print('Successful backup to', target)
# else:
#     print('Backup FAILED')

# M:/Doc_Bk/Python_ML/python-3.8.0-docs-pdf-letter/docs-pdf/tutorial.pdf
#print(f"sys.path = {sys.path}")

print(f"dir = { dir() } \n")
    # dir = ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'builtins', 'sys']

# print(f"dir(sys) = {dir(sys)} \n")
# print(f"dir(builtins) = {dir(builtins)} \n")

print(f"sys.argv = {sys.argv} \n")     # sys.argv = ['m:\\Prj_Py\\Test01\\sys_tst1.py']

print(f"sys.maxsize = { sys.maxsize }")                # sys.maxsize = 9223372036854775807
print(f"sys.float_info.max = { sys.float_info.max}")   # sys.float_info.max = 1.7976931348623157e+308




