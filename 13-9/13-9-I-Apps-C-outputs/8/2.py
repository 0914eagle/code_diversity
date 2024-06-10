
def find_signed_binary_representation(n):
    # Convert the input to a list of digits
    digits = [int(digit) for digit in str(n)]
    # Initialize the minimum number of non-zero digits as the length of the input
    min_non_zero_digits = len(digits)
    # Initialize the minimum representation as the input itself
    min_representation = digits
    # Iterate over all possible representations
    for representation in itertools.product([-1, 0, 1], repeat=len(digits)):
        # Convert the representation to a list of digits
        representation_digits = [int(digit) for digit in representation]
        # Count the number of non-zero digits in the representation
        non_zero_digits = sum(digit != 0 for digit in representation_digits)
        # If the number of non-zero digits is less than the minimum, update the minimum
        if non_zero_digits < min_non_zero_digits:
            min_non_zero_digits = non_zero_digits
            min_representation = representation_digits
    # Return the minimum representation
    return min_representation

def main():
    # Read the input from stdin
    n = int(input())
    # Find the signed binary representation of the input
    representation = find_signed_binary_representation(n)
    # Print the representation
    print("".join(str(digit) for digit in representation))

if __name__ == '__main__':
    main()

