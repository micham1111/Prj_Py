# os_tst2_fileTxt.py  updated: 21_10_02

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
        # Use read() to get everything at once )1()
        text = my_file.read()
        return text

def PrintTxtFile(filePath):   
    print(f"PrintTxtFile:  { filePath }")
    lineNum = 0
    # Open the file for reading
    # You don't have to provide a mode because it is read by default
    with open(filePath, encoding="utf-8") as my_file:
        # We'll use a while loop that loops until the data
        # read is empty
        while True:
            line = my_file.readline()
            # line is empty so exit
            if not line:
                break

            print(f"Line { lineNum } = { line }")
            lineNum += 1



#===============================================================
PATH = "M:/TempM" 

fname = "Temp.txt"

filePath = PATH + "/" + fname
text = "Line1 text\nLine2 text\nLine3 text"

WriteToFile(filePath, text)

textR = ReadFile(filePath)
print(f"textR = { textR }")

# Put the words in a list using the space as
# the boundary between words
word_list = textR.split()
print(f"word_list = { word_list }")

# Get the number of words with len()
nw =  len(word_list)
print(f"len(word_list) = { nw }")



fname2 = "Temp2.txt"

filePath2 = PATH + "/" + fname2

# Rename our file
os.rename(filePath, filePath2)

PrintTxtFile(filePath2)




# Delete a file
# os.remove(filePath2)

# Create a directory
# os.mkdir("mydir")

# Change directories
# os.chdir("mydir")

# Remove a directory, but 1st move back 1 directory
# os.chdir("..")
# os.rmdir("mydir") BE CAREFUL WITH THIS


