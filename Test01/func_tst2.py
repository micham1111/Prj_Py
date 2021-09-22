# func_tst2  updated: 21_09_20


# There is no way to check if a string contains a float so let's make one by defining our own function.
def is_float(str_val):
    try:
        # If the string isn't a float float() will throw a
        # ValueError
        float(str_val)

        # If there is a value you want to return use return
        return True
    except ValueError:
        return False



s = "3.1"
b = is_float(s)
print(f" is_float({ s }) = { b }")

f = 3.14
b = is_float(f)
print(f" is_float({ f }) = { b }")



