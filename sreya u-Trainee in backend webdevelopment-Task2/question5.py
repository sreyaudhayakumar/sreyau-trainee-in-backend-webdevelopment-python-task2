# 5.	Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

user_input = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(user_input)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
