# func_tst3_Recur.py (Recursive) updated: 21_09_28

# Take calculating a factorial as an example 3! = 3 * 2 * 1
def factorial(num):
    # Every recursive function must contain a condition
    # when it ceases to call itself
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


#=================================================================================




f = factorial(3)
print(f" factorial(3) = { f }")    # factorial(3) = 6




