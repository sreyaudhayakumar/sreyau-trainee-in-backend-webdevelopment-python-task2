# 8.Define a function that accepts 2 values and return its sum, subtraction and multiplication. 
#  Using 4 types of functions based on arguments and return type.


# Function Type 1: No arguments, No return type
def calculate():
    num1 = 10
    num2 = 5
    print("Sum:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

calculate()


# Function Type 2: Arguments, No return type
def calculate_witharg(num1, num2):  
    print("Sum:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

calculate_witharg(10, 5)  


# Function Type 3: No arguments, Return type
def calculate_return():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1 + num2, num1 - num2, num1 * num2

result = calculate_return()
print("Result:", result)



# Function Type 4: Arguments, Return type
def calculate_return_with_args(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

result = calculate_return_with_args(10, 5)
print("Result:", result)


