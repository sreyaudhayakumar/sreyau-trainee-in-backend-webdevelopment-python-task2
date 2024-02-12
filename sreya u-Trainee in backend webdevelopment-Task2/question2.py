# 2.Create a function that takes two arguments, a name and an age, and prints a message like "Hello,   [Name]! You are [Age] years old." 
# Call this function with your name and age as arguments.

def person(name, age):
    print("Hello,", user_name , "! You are", user_age, "years old.")

user_name = input("Enter the name: ")
user_age = int(input("Enter the age: "))
person(user_name, user_age)
