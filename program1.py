# Write a Python function that calculates the factorial of a given integer.
# Demonstrate how to call this function with an example. 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("enter a number ; "))
result = factorial(number)
print(f"The factorial of {number} is {result}")

# If the user enters 3, the factorial() function will be called with n = 3.
# The function calculates 3 * factorial(2).
# factorial(2) calculates 2 * factorial(1).
# This continues until factorial(0) is reached, which returns 1.
# So, factorial(1) returns 1 * 1 = 1, factorial(2) returns 2 * 1 = 2, factorial(3) returns 3 * 2 = 6
# Finally, factorial(3) returns 3 * 2 * 1 = 6.
# The program prints: "The factorial of 3 is 6".