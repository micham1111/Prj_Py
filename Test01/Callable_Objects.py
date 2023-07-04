#Callable_Objects.py
# In Python, anything that can be called a function is called a callable object. 
# This includes functions, methods, classes, and even objects that define the __call__ method.

class Adder:
    def __call__(self, x, y):
        return x + y

adder = Adder()
result = adder(3, 4)

print(result)
#7

























