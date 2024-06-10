
def find_signed_binary_representation(n):
    # Initialize the signed binary representation with all zeros
    signed_binary_representation = [0] * (n.bit_length() + 1)

    # Iterate through the binary representation of n
    for i, bit in enumerate(bin(n)[2:]):
        # If the current bit is 1, set the corresponding element in the signed binary representation to 1
        if bit == "1":
            signed_binary_representation[i] = 1

    # Return the signed binary representation
    return signed_binary_representation

def get_minimal_signed_binary_representation(n):
    # Find the signed binary representation of n
    signed_binary_representation = find_signed_binary_representation(n)

    # Initialize the minimal signed binary representation with all zeros
    minimal_signed_binary_representation = [0] * (n.bit_length() + 1)

    # Iterate through the signed binary representation of n
    for i, digit in enumerate(signed_binary_representation):
        # If the current digit is non-zero, set the corresponding element in the minimal signed binary representation to the current digit
        if digit != 0:
            minimal_signed_binary_representation[i] = digit

    # Return the minimal signed binary representation
    return minimal_signed_binary_representation

def main():
    # Read a positive integer n from standard input
    n = int(input())

    # Find the minimal signed binary representation of n
    minimal_signed_binary_representation = get_minimal_signed_binary_representation(n)

    # Print the minimal signed binary representation of n
    print("".join(str(digit) for digit in minimal_signed_binary_representation))

if __name__ == '__main__':
    main()

