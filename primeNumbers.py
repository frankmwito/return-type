def prime_numbers():
    prime_list = []
    num = int(input("Enter size of the list:"))
    
    for i in range(num):
        number = int(input(f"Enter a number for {i+1}:"))
        if number > 1:  # Prime numbers are greater than 1
            is_prime = True
            for j in range(2, int(number ** 0.5) + 1):  # Check divisors up to the square root of the number
                if number % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(number)
    
    return prime_list

# Example Usage
prime_list = prime_numbers()
print(f"The list of prime numbers is: {prime_list}")
