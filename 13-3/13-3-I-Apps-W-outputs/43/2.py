
def solve(a):
    # Convert the input string to a list of digits
    digits = [int(digit) for digit in a]
    # Initialize the minimum integer with the original input
    min_int = digits
    # Loop through each digit in the input
    for i in range(len(digits)):
        # Check if the digit is not the last digit in the input
        if i < len(digits) - 1:
            # Check if the digit and the next digit have different parity
            if digits[i] % 2 != digits[i+1] % 2:
                # Swap the digit with the next digit
                digits[i], digits[i+1] = digits[i+1], digits[i]
                # Check if the resulting integer is smaller than the current minimum
                if int("".join(str(digit) for digit in digits)) < int("".join(str(digit) for digit in min_int)):
                    # Update the minimum integer if necessary
                    min_int = digits
    # Return the minimum integer
    return "".join(str(digit) for digit in min_int)

