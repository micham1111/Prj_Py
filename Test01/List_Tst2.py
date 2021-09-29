# List_Tst2.py  Last updated: 21_09_27  21_09_08  21_08_11


#List
l = [1,2,3,4,5]
print(f"l={ l }")  
print(f"l[2]={ l[2]}")  # 3

# List Comprehension
EvenSqr = [x*x for x in l if x % 2 == 0]
print(f"EvenSqr={ EvenSqr }")  # EvenSqr=[4, 16]



# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

squares = [x**2 for x in range(10)]
print(f"squares={ squares }")
   # squares=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


pairs =[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f"pairs={ pairs }\n")
    # pairs=[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


# learning-scientific-programming-python-2nd.pdf
list1 = [1, 'two', 3.14 , 0]
print(f"list1={ list1 }")  

a = 4
list2 = [2, a, -0.1, list1 , True]
print(f"list2={ list2 }\n")  
     # list2=[2, 4, -0.1, [1, 'two', 3.14, 0], True]

list1[2] = 2.7
print(f"list1={ list1 }")  # list1=[1, 'two', 2.7, 0]
print(f"list2={ list2 }")  # list2=[2, 4, -0.1, [1, 'two', 2.7, 0], True]


q1 = [x for x in range(1,7,2)]  
print(f"q1={ q1 }\n")    # q1=[1, 3, 5]

q2 = q1   # q1 and q2 refer to the same list, lists are mutable
q1[2] = 'oops'
print(f"q1={ q1 }")      # q1=[1, 3, 'oops']
print(f"q2={ q2 }\n")    # q2=[1, 3, 'oops']

q2[1] = 'oops2'
print(f"q1={ q1 }")      # q1=[1, 'oops2', 'oops']
print(f"q2={ q2 }\n")    # q2=[1, 'oops2', 'oops']

q = [x for x in range(1,5)]  
print(f"q={ q }\n")    # q=[1, 2, 3, 4]

# Insert value at index insert(index, value)
q.insert(2, 6)
print(f"q.insert(2, 6)={ q }\n")    # q.insert(2, 6)=[1, 2, 6, 3, 4]

# Delete first occurrence of value
q.remove(3)
print(f"q.remove(3)={ q }\n")    # q.remove(3)=[1, 2, 6, 4]

# Remove item at index
q.pop(2)
print(f"q.pop(2) = { q }\n")    # q.pop(2)=[1, 2, 4]

# Create the multidimensional list 3 x 14
mult_table = [[0] * 4 for i in range(3)]
print(f"mult_table = { mult_table }\n")    # mult_table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# This will increment for each row
for i in range(0, 3):
    # This will increment for each item in the row
    for j in range(0, 4):
        # Assign the value to the cell
        mult_table[i][j] = i * j

print(f"mult_table = { mult_table }\n")
