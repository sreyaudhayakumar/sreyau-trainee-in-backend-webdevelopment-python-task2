# 6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 

def is_prime(num):
    if num < 2:
        return "Not prime number"
    for i in range(2, num):
        if num % i == 0:
            return "Not prime number"
    return "Is Prime number"


number = int(input("Enter a number: "))
print("Result:", is_prime(number))
