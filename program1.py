# Write a Python function that calculates the factorial of a given integer.
# Demonstrate how to call this function with an example. 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("enter a number"))
result = factorial(number)
print(f"The factorial of {number} is {result}")

    