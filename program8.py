# Define a function that accepts 2 values and return its sum, subtraction and multiplication.
# Using 4 types of functions based on arguments and return type

# 1)Function  with arguments and with return type
def calculate_operations(value1, value2):
    sum_result = value1 + value2
    subtraction_result = value1 - value2
    multiplication_result = value1 * value2
    return sum_result, subtraction_result, multiplication_result
value1 = 10
value2 = 5
sum_result, subtraction_result, multiplication_result = calculate_operations(value1, value2)
print(f"Sum: {sum_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")

# 2)Function  with arguments and without return type
def perform_operations(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b

    print(f"Sum: {sum_result}")
    print(f"Subtraction: {sub_result}")
    print(f"Multiplication: {mul_result}")
value1 = 10
value2 = 5
perform_operations(value1, value2)

# 3)Function without default arguments and return value:
def perform_operations():
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))
    
    addition = value1 + value2
    subtraction = value1 - value2
    multiplication = value1 * value2
    
    return addition, subtraction, multiplication
add_result, sub_result, mul_result = perform_operations()
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)

# 4)without argument without return type

def perform_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Sum:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

perform_operations()
