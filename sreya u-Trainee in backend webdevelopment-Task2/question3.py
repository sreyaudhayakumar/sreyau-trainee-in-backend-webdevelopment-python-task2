# 3.	Write a Python function to find the maximum of three numbers

def maximum(num1, num2, num3):
    maximum_value = max(num1, num2, num3)
    return maximum_value

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print("Maximum of the three numbers:", maximum(num1, num2, num3))
