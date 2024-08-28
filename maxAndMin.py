# return a list of maximum and minimum numbers in a list

def maxand_min():
    numbers = list()
    num = int(input("Enter the size of your list:"))
    
    for i in range(num):
        number = int(input(f"Enter a number {i+1}:"))
        numbers.append(number)
    
    max_num = max(numbers)
    print(max_num)
    min_num = min(numbers)
    return min_num
print(maxand_min())