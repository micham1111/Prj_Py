# map_Tst1.py  Last updated: 21_11_06

# The function to pass into map
def dbl_num(num):
    return num * 2

#===================

# Generate a list from 1 to 4
list1_4 = list(range(1, 5))
print(f"list1_4={ list1_4 }")


mapI_L = map(dbl_num, list1_4)
listI_L = list(mapI_L)
#print(f"mapI_L={ mapI_L }")
#listI_L = list(map(dbl_num, list1_4))
print(f"listI_L={ listI_L }")

# You can perform calculations against multiple lists
list_a = list(map((lambda x, y: x + y), [1, 2, 3], [4, 5, 6]))
print(f"list_a={ list_a }")





