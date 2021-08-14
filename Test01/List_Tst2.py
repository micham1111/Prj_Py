# List_Tst2.py  Last updated:   21_08_11

#List
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

squares = [x**2 for x in range(10)]
print(f"squares={ squares }")


pairs =[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f"pairs={ pairs }\n")
