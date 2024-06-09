
def solve(n, x, y, number):
    # Convert the number to a list of digits
    number = [int(digit) for digit in number]
    
    # Initialize the minimum number of operations to perform
    min_operations = 0
    
    # Iterate over the digits of the number
    for i in range(n):
        # If the current digit is 0, flip it to 1
        if number[i] == 0:
            number[i] = 1
            min_operations += 1
        # If the current digit is 1 and it is not the last digit, flip it to 0
        elif number[i] == 1 and i < n-1:
            number[i] = 0
            min_operations += 1
    
    # Return the minimum number of operations to perform
    return min_operations

