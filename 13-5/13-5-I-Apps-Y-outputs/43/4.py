
def solve(n, x, y, number):
    # Convert the number to a list of digits
    number = [int(digit) for digit in number]
    
    # Initialize the minimum number of operations to perform
    min_operations = 0
    
    # Iterate over the digits of the number
    for i in range(n):
        # If the current digit is 0 and the next digit is 1, flip the current digit
        if number[i] == 0 and i < n-1 and number[i+1] == 1:
            number[i] = 1
            min_operations += 1
    
    # Return the minimum number of operations to perform
    return min_operations

