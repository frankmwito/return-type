# find the greatest common divisor 
# two integers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
print(gcd(a, b))