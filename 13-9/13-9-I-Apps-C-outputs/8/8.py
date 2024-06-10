
def get_signed_binary_representation(n):
    # Convert the input to a binary string
    binary_str = bin(n)[2:]
    
    # Initialize the signed binary representation as a list of zeros
    signed_binary_repr = [0] * len(binary_str)
    
    # Loop through the binary string and convert each digit to -1, 0, or 1
    for i, digit in enumerate(binary_str):
        if digit == "0":
            signed_binary_repr[i] = 0
        elif digit == "1":
            signed_binary_repr[i] = 1
        else:
            signed_binary_repr[i] = -1
    
    # Return the signed binary representation as a string
    return "".join(str(digit) for digit in signed_binary_repr)

def get_minimal_signed_binary_representation(n):
    # Get the signed binary representation of the input number
    signed_binary_repr = get_signed_binary_representation(n)
    
    # Initialize the minimal signed binary representation as the current signed binary representation
    minimal_signed_binary_repr = signed_binary_repr
    
    # Loop through the signed binary representation and check if any digit can be changed to a smaller digit
    for i in range(len(signed_binary_repr)):
        if signed_binary_repr[i] == 1:
            # If the digit is 1, change it to -1 and check if the resulting representation is smaller
            signed_binary_repr[i] = -1
            if len(signed_binary_repr) < len(minimal_signed_binary_repr):
                minimal_signed_binary_repr = signed_binary_repr
            signed_binary_repr[i] = 1
    
    # Return the minimal signed binary representation as a string
    return "".join(str(digit) for digit in minimal_signed_binary_repr)

if __name__ == '__main__':
    n = int(input())
    print(get_minimal_signed_binary_representation(n))

