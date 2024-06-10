
def get_signed_binary_representation(n):
    # Initialize the signed binary representation with all zeros
    signed_binary_representation = [0] * (n.bit_length() + 1)

    # Iterate through the bits of the input number
    for i in range(n.bit_length()):
        # If the current bit is set, set the corresponding signed binary representation bit to +1
        if n & (1 << i):
            signed_binary_representation[i] = 1
        # If the current bit is not set, set the corresponding signed binary representation bit to -1
        else:
            signed_binary_representation[i] = -1

    # Return the signed binary representation
    return signed_binary_representation

def get_minimal_signed_binary_representation(n):
    # Get the signed binary representation of the input number
    signed_binary_representation = get_signed_binary_representation(n)

    # Initialize the minimal signed binary representation with all zeros
    minimal_signed_binary_representation = [0] * len(signed_binary_representation)

    # Iterate through the bits of the signed binary representation
    for i in range(len(signed_binary_representation)):
        # If the current bit is non-zero, set the corresponding minimal signed binary representation bit to the current bit
        if signed_binary_representation[i] != 0:
            minimal_signed_binary_representation[i] = signed_binary_representation[i]
        # If the current bit is zero, set the corresponding minimal signed binary representation bit to the previous bit
        else:
            minimal_signed_binary_representation[i] = minimal_signed_binary_representation[i - 1]

    # Return the minimal signed binary representation
    return minimal_signed_binary_representation

def main():
    # Read a line of input from stdin and convert it to an integer
    n = int(input().strip())

    # Get the minimal signed binary representation of the input number
    minimal_signed_binary_representation = get_minimal_signed_binary_representation(n)

    # Print the minimal signed binary representation
    print("".join(str(x) for x in minimal_signed_binary_representation))

if __name__ == '__main__':
    main()

