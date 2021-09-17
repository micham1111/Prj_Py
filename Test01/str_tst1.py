# Str_Tst1.py  updated: 21_09_17

first_name ='Chris'
last_name = 'Harrison'
str1 =  'Hello {}  {}'.format(first_name, last_name)
# Python 3
str2 = f'Hello {first_name} {last_name}'
print(str2)

number = 20
str3 = str(number)
print(str3)

str4 = first_name.lower()
print(str4)

# https://docs.python.org/3/tutorial/index.html
print(r'C:\some\name')  # note the r before the quote


# P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6   Index
#-6  -5  -4  -3  -2  -1
word = 'Python'
print(word[0])  # character in position 0

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:])
print(word[-1])  # last character

print(word[-2])  # second-last character
        # 'o'
print(word[-6])
         #'P'
print(word[0:-1:2])
print(word[::-1])

print(word[:2] + word[2:])
print(word[-2:])  # characters from the second-last (included) to the end
        # 'on'
print(len(word))

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
print()


x = 'Pluto is a planet'
y = "Pluto is a planet"
b = x == y
print(f"b = {b}")

s1 = 'Pluto\'s a planet!'
print(f"s1 = {s1}")
print(f"s1.index = {s1.index('planet')}")


s2 = "hello\nworld"
print(f"s2 = {s2}")


s3 = 'Pluto'
print(f"len( {s3 }) = { len(s3) }")
l = [char+'! ' for char in s3]
print(f"l = {l}")

# ALL CAPS
s4 = s3.upper()
print(f"s4 = {s4}")

# all lowercase
s5 = s3.lower()
print(f"s5 = {s5}")


s6 = "Pluto is a planet!"
s7 = "planet!"
b = s6.startswith(s3)
print(f"b = {b}")

b2 = s6.startswith(s7)
print(f"b2 = {b2}")

b3 = s6.endswith(s7)
print(f"b3 = {b3}")

s8 = s3 + ', we miss you.'
print(f"s8 = {s8}")

i = 9
s9 = s3 + str(i) 
print(f"s9 = {s9}")

s10 = "{}, you'll always be the {}th planet to me.".format(s3, i)
print(f"s10 = {s10}")

fl = 10.12345
s11 = "fl equalto {:.3}".format(fl)
print(f"s11 = {s11}")

words = s6.split()
print(f"words = {words}")

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(f"year={year},  month={month},  day={day} ")

datestr2 = '/'.join([month, day, year])
print(f"datestr2 = {datestr2}")


fn = 'Inc0_16x16.f32'
print(f"fn = { fn }")
print(f"fn[-4] = { fn[-4] }")   # fn[-4] = .

# Repeat strings with *
print("Hello " * 5)




