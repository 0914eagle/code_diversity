
def solve(k, n):
    # Find the number of digits in n
    num_digits = len(str(n))
    # Initialize a counter for the minimum number of digits that can differ
    min_diff = 0
    # Iterate through each digit in n
    for i in range(num_digits):
        # Get the current digit
        digit = int(str(n)[i])
        # If the current digit is not equal to the corresponding digit in k, increment the counter
        if digit != k % 10:
            min_diff += 1
        # Update k to remove the current digit
        k //= 10
    # Return the minimum number of digits that can differ
    return min_diff

