#This code calculates a factorial of a any positive number 
#The user is asked to enter a number then a factorial of that number is given back as an answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a non-negative integer: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")
