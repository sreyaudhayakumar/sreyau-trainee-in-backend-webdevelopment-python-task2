# 4.	Write a Python program to reverse a string

def reverse_string(string):
    rev_str = string[::-1]
    return rev_str

user_input = input("Enter the string: ")
reversed_string = reverse_string(user_input)
print("Original string:", user_input)
print("Reversed string:", reversed_string)
