
def solve(n, x, y, num):
    # Convert the number to a list of digits
    num = list(map(int, num))
    # Initialize the minimum number of operations to perform
    min_operations = 0
    # Loop through the digits of the number
    for i in range(n):
        # If the current digit is 0, flip it to 1
        if num[i] == 0:
            num[i] = 1
            min_operations += 1
        # If the current digit is 1 and it is not the last digit, flip it to 0
        elif num[i] == 1 and i < n-1:
            num[i] = 0
            min_operations += 1
    # Return the minimum number of operations to perform
    return min_operations

