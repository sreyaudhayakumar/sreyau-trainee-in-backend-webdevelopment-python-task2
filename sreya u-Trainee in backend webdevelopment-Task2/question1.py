# 1.Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example

def factorial(user_input):
    fact = 1
    for i in range(1, user_input + 1):
        fact *= i
    return fact

user_input = int(input("Enter the value: "))
result = factorial(user_input)
print("Factorial of", user_input, "=", result)
