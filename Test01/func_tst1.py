# updated: 20_04_05
# M:/Doc_Bk/Python_ML/python-3.8.0-docs-pdf-letter/docs-pdf/tutorial.pdf

#Function
def func(x):
    if x==0:
        return x+1
    elif x > 0:
        return x-1
    else:
	    return x

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

# M:/Doc_Bk/Python_ML/python-3.8.0-docs-pdf-letter/docs-pdf/tutorial.pdf
def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

#================================================
x = 0
y = func(x)
print(f" func({x}) = { y }")

x = 3
y = func(x)
print(f" func({x}) = { y }")


x = -1
y = func(x)
print(f" func({x}) = { y }\n")


print("Calc = ", call(mult_by_five, 2))


def count_negatives(nums):
    """Return the number of negative numbers in the given list.    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives2(nums):
    return len([num for num in nums if num < 0])

def count_negatives3(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

cn = count_negatives([5, -1, -2, 0, 3, -5])
print(f"cn = {cn}")

cn2 = count_negatives2([5, -1, -2, 0, 3, -5])
print(f"cn2 = {cn2}")

cn3 = count_negatives3([5, -1, -2, 0, 3, -5])
print(f"cn3 = {cn3}")


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


fl = fib2(100)
print(f"fl = {fl}")
print()

s = 'abcd'
r = reverse(s)
print(f" reverse({ s }) = { r } \n")


s = 'abcba'
p = is_palindrome(s)
print(f" is_palindrome({ s })  = { p } \n")

r = divide(6, 2)
r = divide(6, 0)
#r = divide("6", "2")


