# os_tst2_fileTxt.py  updated: 21_09_28

# Writing Text to a File

# The os module provides methods for file processing
import os

def WriteToFile(filePath, text):
    print(f"filePath= { filePath}")
    # the code withwhich guarantees the file
    # will be closed if the program crashes
    with open(filePath, mode="w", encoding="utf-8") as myFile:
        # You can write to the file with write
        # It doesn't add a newline
        myFile.write(text)

def ReadFile(filePath):   
    # Open the file for reading
    # You don't have to provide a mode because it is read by default
    with open(filePath, encoding="utf-8") as my_file:
        # We can read data in a few ways
        # 1. read() reads everything into 1 string
        # 2. readline() reads everything including the first newline
        # 3. readlines() returns a list of every line which includes
        # each newline   
        text = my_file.read()
        return text



#===============================================================
PATH = "M:/TempM" 

fname = "Temp.txt"

filePath = PATH + "/" + fname
text = "Line1 text\nLine2 text\nLine3 text"

WriteToFile(filePath, text)

textR = ReadFile(filePath)
print(f"textR = { textR }")








