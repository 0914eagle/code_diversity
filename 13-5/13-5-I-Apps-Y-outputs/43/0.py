
def solve(n, x, y, number):
    # Initialize the minimum number of operations to perform
    min_operations = 0
    # Initialize the current number
    current_number = number
    # Loop through each digit of the number
    for i in range(n):
        # If the current digit is 0, flip it to 1
        if current_number[i] == "0":
            current_number = current_number[:i] + "1" + current_number[i+1:]
            min_operations += 1
        # If the current digit is 1 and it is not the last digit, flip it to 0
        elif current_number[i] == "1" and i < n-1:
            current_number = current_number[:i] + "0" + current_number[i+1:]
            min_operations += 1
    # Return the minimum number of operations to perform
    return min_operations

