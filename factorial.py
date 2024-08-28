# calculate the factorial of a number and return the result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter any number:"))
result = factorial(n)

print("The factorial of the number is:", result)