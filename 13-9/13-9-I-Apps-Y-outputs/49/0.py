
def max_divisible_by_3(s):
    # Convert the input string to a list of digits
    digits = [int(digit) for digit in s]
    # Initialize the maximum number of divisible numbers to 0
    max_divisible = 0
    # Loop through all possible cuts
    for i in range(len(digits)):
        # Get the current digit
        digit = digits[i]
        # Check if the current digit is divisible by 3
        if digit % 3 == 0:
            # If the current digit is divisible by 3, increment the maximum number of divisible numbers
            max_divisible += 1
        # If the current digit is not divisible by 3, check if the previous digit is divisible by 3
        elif i > 0 and digits[i-1] % 3 == 0:
            # If the previous digit is divisible by 3, increment the maximum number of divisible numbers
            max_divisible += 1
    # Return the maximum number of divisible numbers
    return max_divisible

