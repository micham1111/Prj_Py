# Str_Tst2.py  updated: 21_09_17


# Strings have many methods we can use beyond what I covered last time
str1 = "   this is an important string   "
print(f" str1 = { str1 }")    

# Delete whitespace on left
str2 = str1.lstrip()
print(f" str1.lstrip() = { str2 }")   # str1.lstrip() = this is an important string  

# Delete whitespace on right
str3 = str1.rstrip()
print(f" str1.rstrip() = { str3 }")   #  str1.rstrip() =    this is an important string

# Delete whitespace on right and left
str4 = str1.strip()
print(f" str4.strip() = { str4 }")  # str4.strip() = this is an important string

# Capitalize the 1st letter
str5 = str4.capitalize()
print(f" str4.capitalize() = { str5 }")  # str4.capitalize() = This is an important string

# Capitalize every letter
str6 = str1.upper()
print(f" str1.upper() = { str6 }")  # str1.upper() =    THIS IS AN IMPORTANT STRING

# lowercase all letters
str7 = str6.lower()
print(f" str6.lower() = { str7 }")   #  str6.lower() =    this is an important string  

# We can find how many times a string occurs in a string
s = "is"
c = str7.count(s)
print(f"  str7.count({ s }) = { c }")   # str7.count(is) = 2

a_list_2 = str7.split()
print(f"  str7.split() = { a_list_2 }")
        # str7.split() = ['this', 'is', 'an', 'important', 'string']

# Get an index for a matching string
i = str4.find(s)
print(f" str4.find({ s }) = { i } ")   #  str4.find(is) = 2

# Replace a string
str8 = "aa bb cc bb"
s1 = "bb"
s2 = "dd"
str9 = str8.replace(s1, s2)
print(f" str9 = str8.replace({s1}, {s2}) = { str9 }")  # str9 = str8.replace(bb, dd) = aa dd cc dd

c1 = "z"
# Returns True if characters are letters or numbers
# Whitespace is false
b = c1.isalnum() 
print(f"Is { c1 } a letter or number : {  b } ")  # Is z a letter or number : True

# Returns True if characters are letters
b = c1.isalpha()
print(f"Is { c1 } a letter: {  b } ")  # 










