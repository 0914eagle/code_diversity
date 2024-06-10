
def get_signed_binary_representation(n):
    # Initialize the signed binary representation with all zeros
    signed_representation = [0] * 100000

    # Convert the input number to binary
    binary_representation = bin(n)[2:]

    # Loop through the binary representation and convert it to signed binary representation
    for i, digit in enumerate(binary_representation):
        if digit == "1":
            signed_representation[i] = 1
        elif digit == "0":
            signed_representation[i] = 0
        else:
            signed_representation[i] = -1

    # Return the signed binary representation
    return signed_representation

def get_minimal_signed_binary_representation(n):
    # Get the signed binary representation of the input number
    signed_representation = get_signed_binary_representation(n)

    # Initialize the minimal signed binary representation with all zeros
    minimal_signed_representation = [0] * 100000

    # Loop through the signed binary representation and find the minimal representation
    for i, digit in enumerate(signed_representation):
        if digit != 0:
            minimal_signed_representation[i] = digit
            break

    # Return the minimal signed binary representation
    return minimal_signed_representation

if __name__ == '__main__':
    n = int(input())
    minimal_signed_representation = get_minimal_signed_binary_representation(n)
    print("".join([str(digit) for digit in minimal_signed_representation]))

