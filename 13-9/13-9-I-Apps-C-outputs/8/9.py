
def get_signed_binary_representation(n):
    # Initialize the signed binary representation with all zeros
    signed_binary_representation = [0] * 100000

    # Convert the input to a binary string
    binary_string = bin(n)[2:]

    # Iterate through the binary string and assign the corresponding values to the signed binary representation
    for i, digit in enumerate(binary_string):
        if digit == "1":
            signed_binary_representation[i] = 1
        elif digit == "0":
            signed_binary_representation[i] = 0
        else:
            signed_binary_representation[i] = -1

    # Return the signed binary representation with the minimal number of non-zero digits
    return "".join(str(digit) for digit in signed_binary_representation if digit != 0)

def main():
    n = int(input())
    print(get_signed_binary_representation(n))

if __name__ == '__main__':
    main()

