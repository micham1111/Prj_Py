# List_Tst3.py  Last updated: 21_11_06

import random

# You must import reduce
from functools import reduce

list1_4 = list(range(1, 5))
print(f"list1_4={ list1_4 }")

# Filter

# While map executes functions on a list, filter selects items from a list based on a function
# Print out the even values from a list
list1_10 = range(1, 11)
listF = list(filter((lambda x: x % 2 == 0), list1_10))
print(f"listF={ listF }")

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
rand_list = list(random.randint(1, 10) for i in range(5))
print(f"rand_list={ rand_list }")


# Add up the values in a list
SumL = reduce((lambda x, y: x + y), list1_4)  # 1 + 2 + 3 + 4 = 10
print(f"SumL={ SumL }")   


