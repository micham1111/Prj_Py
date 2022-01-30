# "D:\Bk_Doc_Test\Python\python-programming-bootcamp-video21\01.2 All Code Files\All Code Files\pythontut27.py"

import re


# We saw that . matches any character, but what if we want to match a period
# Backslash the period. You do the same with [, ] and others.
rand_str = "F.B.I. I.R.S. CIA"
#print("Matches :", len(re.findall(".\..\..", rand_str)))
str = re.findall(".\..\..", rand_str)
Matches = len(str)
print(f"rand_str= {rand_str}, Matches={ Matches }, str={ str }")  # rand_str= F.B.I. I.R.S. CIA, Matches=2, str=['F.B.I', 'I.R.S']   ?????


# We can match many whitespace characters
rand_str = """This is a long
string that goes
on for many lines"""
print(f"rand_str= {rand_str}")

# Remove newlines
regex = re.compile("\n")
rand_str_n = regex.sub(" ", rand_str)
print(f"rand_str_n= {rand_str_n}")


# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab
# You may need to remove \r\n on Windows

# Matching Any Single Number

# \d can be used instead of [0-9]
# \D is the same as [^0-9]
rand_str = "begin12345end"
#print("Matches :", len(re.findall("\d", rand_str)))
str = re.findall("\d", rand_str)
Matches = len(str)
print(f"rand_str={ rand_str }, str={ str },  Matches={ Matches }")   # rnd_str=begin12345end, str=['1', '2', '3', '4', '5'],  Matches=5


# You can match multiple digits by following the \d with {numOfValues}
# Match 5 numbers only
#if re.search("\d{5}", "12345"):
 #   print("It is a zip code")
flag = re.search("\d{5}", rand_str)
print(f"rand_str={ rand_str }, flag={ flag }")   # rand_str=begin12345end, flag=<re.Match object; span=(5, 10), match='12345'>

# You can also match within a range
# Match values that are between 5 and 7 digits
num_str = "123 12345 123456 1234567"

print("Matches :", len(re.findall("\d{5,7}", num_str)))






