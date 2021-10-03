# Tuple_tst1.py  updated: 21_10_02

# Tuples

# A Tuple is like a list, but their values can't be changed
# Tuples are surrounded with parentheses instead of square brackets

a = (5,6)
print(f"a = {a}")   # a = (5, 6)
print(f"type(a) = { type(a) }\n")   # tuple
# Get the number of items in a Tuple
n = len(a)
print(f"Tuple Length: len(a) = { n } ")  # Tuple Length: len(a) = 2

t = (1, 2, 3, 4)   
print(f"t = {t}")    # t = (1, 2, 3, 4)

#t[0] = 100    error
print(f"t[0] = {t[0]}")    # t[0] = 1

it = 3
b = it in t
print(f"it in t = { b }")    # it in t = True

# Get a slice from the 1st index up to but not including the 3rd
st = t[0:3]
print(f"t[0:2] = {st}")    # t[0:2] = (1, 2, 3)

# Join or concatenate tuples
a_st = a + st
print(f"a + st = { a_st}")    # a + st = (5, 6, 1, 2, 3)



# Convert a List into a Tuple
a_list = [55, 89, 144]
a_tuple = tuple(a_list)
print(f"a_tuple = { a_tuple }")

# Get max and minimum value
mi = min(a_tuple)
print(f" min(a_tuple) = { mi } ")
ma = max(a_tuple)
print(f" max(a_tuple) = { ma } ")


# Convert a Tuple into a List
a_list2 = list(a_tuple)
print(f"a_list2 = { a_list2 }")





x = 0.125
numerator, denominator = x.as_integer_ratio()
print(f"x = {x},    x.as_integer_ratio = {x.as_integer_ratio()} \n")  # x = 0.125,   x.as_integer_ratio = (1, 8)

multiplicands = (2, 2, 3, 3)
product = 1
for mult in multiplicands:
    product = product * mult
print(f"product = {product}")   # product = 36 ()= 1 * 2 * 2 * 3 * 3)


