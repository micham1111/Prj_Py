# List_Tst3.py  Last updated: 21_11_06

import random

# You must import reduce
from functools import reduce

list1_4 = list(range(1, 5))      # list1_4=[1, 2, 3, 4]
print(f"list1_4={ list1_4 }")

# Filter
# While map executes functions on a list, filter selects items from a list based on a function
# Print out the even values from a list
list1_10 = range(1, 11)   # 1 2 3 4 5 6 7 8 9 10
listF = list(filter((lambda x: x % 2 == 0), list1_10))    # listF=[2, 4, 6, 8, 10]
print(f"listF={ listF }")

# With a list comprehension we'd do
# Note that a list comprehension is surrounded by []
# because it returns a list
listEven = [2 * x for x in range(1, 11)]
print(f"listEven={ listEven }")   # listEven=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 


# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
rand_list = list(random.randint(1, 10) for i in range(5))   #  rand_list=[5, 6, 7, 9, 4]
print(f"rand_list={ rand_list }")


# Add up the values in a list
SumL = reduce((lambda x, y: x + y), list1_4)  # 1 + 2 + 3 + 4 = 10
print(f"SumL={ SumL }")      # SumL=10

# Video 25:
# To multiply 2 times every value with a map we'd do
#print(list(map((lambda x: x * 2), range(1, 11))))
#mp = map((lambda x: x * 2), range(1, 11))
#print(f"mp = { mp } ") 
list2_10 = list(map((lambda x: x * 2), range(1, 11)))
print(f"list2_10 = { list2_10 } ")   # ist2_10 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# A list comprehension can act as map and filter
# on one line
# Generate a list of 50 values and take them to the power
# of 2 and return all that are multiples of 8
list8 = [i ** 2 for i in range(50) if i % 8 == 0]
print(f"list8 = { list8 } ")   # list8 = [0, 64, 256, 576, 1024, 1600, 2304]

# You can have multiple for loops as well
# Multiply all values in one list times all values in
# another
list2d_0 = [x * y for x in range(1, 3) for y in range(11, 16)]
print(f"list2d_0 = { list2d_0 } ")   # 


fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits): 
    print(index, fruit)
#0 apple
#1 banana
#2 mango


