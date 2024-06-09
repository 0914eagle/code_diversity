
def solve(v, a):
    # Initialize a list to store the maximum number that can be written for each digit
    max_num = [0] * 10
    # Loop through the given numbers and find the maximum number that can be written for each digit
    for i in range(1, 10):
        # Check if the current digit is not a zero
        if i != 0:
            # Find the maximum number that can be written for the current digit
            max_num[i] = min(v // a[i], 9)
            # Update the remaining volume of paint
            v -= max_num[i] * a[i]
    
    # Initialize a variable to store the maximum number that can be written
    max_total = 0
    # Loop through the maximum numbers that can be written for each digit
    for i in range(1, 10):
        # Check if the current digit is not a zero
        if i != 0:
            # Add the current digit to the maximum number that can be written
            max_total = max_total * 10 + max_num[i]
    
    # Return the maximum number that can be written
    return max_total if v == 0 else -1

