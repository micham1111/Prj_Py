# Generators_Tst.py

### Generators created using yield keyword 
def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Driver code to check above generator function 
for number in fibonacci_series(10):
    print(number)

#0
#1
#1
#2
#3
#5
#8
#13
#21
#34











