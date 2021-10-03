# Os_Tst1.py   updated: 21_09_11  20_04_05
# M:/Doc_Bk/Python_ML/python-3.8.0-docs-pdf-letter/docs-pdf/tutorial.pdf

import os
import shutil
import glob


os_version = os.getenv('OS')
print(os_version)
   # WINDOWS_NT

s = os.getcwd()
print(f"os.getcwd = { s }\n")   # Display current directory
     # os.getcwd = M:\Prj_Py\Test01

# os.chdir('/server/accesslogs') # Change current working directory
# .system('mkdir today') # Run the command mkdir in the system shell
# print(f"dir(os) = { dir(os) }") 

# shutil file and directory management tasks
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# The glob module provides a function for making file lists from directory wildcard searches:
s1 = glob.glob('*.py')
print(f"glob = { s1 } \n")
   # glob = ['Complex_Tst1.py', 'List_tst1.py', 'List_Tst2.py', 'numpy_Files.py', 'numpy_Files_Func.py', 'numpy_random_tst.py', 'numpy_tst1.py', 'numpy_tst2.py', 'numpy_tst3_Ar2d.py', 'os_tst1.py', 'Pil_tst1.py']
################
dir_img =  "M:/DB/Im_RGB/"
fn_img =  "bird.jpg"
path_img = dir_img + fn_img

s2 = os.path.splitext(path_img)
print(f"os.path.splitext(path_img) = { s2 }")
     # os.path.splitext(path_img) = ('M:/DB/Im_RGB/bird', '.jpg')
s3 = os.path.splitext(path_img)[0]
print(f"os.path.splitext(path_img)[0] = { s3 }")
     # os.path.splitext(path_img)[0] = M:/DB/Im_RGB/bird
s4 = os.path.splitext(path_img)[1]
print(f"os.path.splitext(path_img)[1] = { s4 } \n")
     # os.path.splitext(path_img)[1] = .jpg

