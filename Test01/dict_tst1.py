# dict_tst1.py    21_09_28  20_03_29

#dictionary
numbers = {'one':1, 'two':2, 'three':3}
# Dictionaries may not print out in the order created since they are unordered
print(f"numbers = { numbers }")   # numbers = {'one': 1, 'two': 2, 'three': 3}
print(f"numbers['two'] = { numbers['two'] } ")  # numbers['two'] = 2

# Get the list of values
print(f"numbers.values() = { numbers.values() }") # numbers.values() = dict_values([1, 2, 3])

# Get the list of keys
print(f"numbers.keys() = { numbers.keys() }")  # numbers.keys() = dict_keys(['one', 'two', 'three'])



# Add a new key value
numbers['eleven'] = 11
print(f"numbers (add 11) = { numbers }")  # numbers (add 11) = {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}

b = 'eleven' in numbers
print(f"eleven in numbers = { b }")  # eleven in numbers = True


# Get gets a value associated with a key or the default
MyKey = "three"
result = numbers.get(MyKey, "Not Here")
print(f"numbers.get({ MyKey }, Not Here) = { result }")   # numbers.get(three, Not Here) = 3

MyKey = "five"
result = numbers.get(MyKey, "Not Here")
print(f"numbers.get({ MyKey }, Not Here) = { result }")   # numbers.get(five, Not Here) = Not Here


# Delete a key value
del numbers['two']
print(f"del numbers[two] = { numbers }")   # del numbers[two] = {'one': 1, 'three': 3, 'eleven': 11}

# Loop through the dictionary keys
print("numbers (Loop):") 
for k in numbers:
    print(k)
       # one
       # three
       # eleven


print("numbers.format:") 
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
       # one = 1
       # two = 2
       # three = 3
       # eleven = 11

# Get the key and value with items()
print("numbers.items:") 
for k, v in numbers.items():
    print(k, v)
      # one 1
      # two 2
      # three 3
      # eleven 11

# Delete all entries
numbers.clear()      

#=====================================================================
# M:/Doc_Bk/Python_ML/byte-of-python.pdf

points = [{'x': 2, 'y': 3},
           {'x': 4, 'y': 1}]
print(f"points = {points}")   # points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]

points.sort(key=lambda i: i['y'])
print(f"points(sorted) = {points}")  # points(sorted) = [{'x': 4, 'y': 1}, {'x': 2, 'y': 3}]


