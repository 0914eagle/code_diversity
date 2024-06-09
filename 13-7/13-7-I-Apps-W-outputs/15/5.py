
def solve(k, n):
    # Convert the integer n to a list of individual digits
    digits = [int(digit) for digit in str(n)]
    # Initialize a counter for the minimum number of digits that can differ
    min_diff = 0
    # Iterate through the digits of n
    for i in range(len(digits)):
        # If the digit is not equal to the corresponding digit of the initial number, increment the counter
        if digits[i] != k % 10:
            min_diff += 1
        # Update the value of k to remove the current digit
        k //= 10
    # Return the minimum number of digits that can differ
    return min_diff

