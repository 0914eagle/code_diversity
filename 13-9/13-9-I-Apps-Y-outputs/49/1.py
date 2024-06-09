
def solve(s):
    # Convert the input string to a list of digits
    digits = [int(digit) for digit in s]
    # Initialize a variable to store the maximum number of divisible numbers
    max_divisible = 0
    # Loop through each possible cut position
    for cut in range(len(digits)):
        # Calculate the number of digits to the left and right of the cut
        left_digits = digits[:cut]
        right_digits = digits[cut:]
        # Check if the number of digits to the left is not zero
        if left_digits:
            # Check if the number of digits to the left is divisible by 3
            if sum(left_digits) % 3 == 0:
                max_divisible += 1
        # Check if the number of digits to the right is not zero
        if right_digits:
            # Check if the number of digits to the right is divisible by 3
            if sum(right_digits) % 3 == 0:
                max_divisible += 1
    return max_divisible

