# reverse a string

def reversed_string():
    s = input("Enter a string:")
    reversed_str = "".join(reversed(s))
    return reversed_str 

print(reversed_string())