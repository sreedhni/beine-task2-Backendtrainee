# Write a Python function to find the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)

num1 = int(input("enter the number1: "))
num2 = int(input("enter the number2; "))
num3 = int(input("enter the number3; "))

maximum = max_of_three(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")
