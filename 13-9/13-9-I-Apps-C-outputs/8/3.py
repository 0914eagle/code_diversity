
def convert_to_signed_binary(n):
    # Convert the input number to a binary string
    binary_str = bin(n)[2:]
    # Initialize the signed binary string with the corresponding sign
    signed_binary_str = '+' if n > 0 else '-' if n < 0 else '0'
    # Iterate through the binary string and append the corresponding sign to the signed binary string
    for bit in binary_str:
        signed_binary_str += '+' if bit == '1' else '-' if bit == '0' else '0'
    return signed_binary_str

def get_minimal_signed_binary(n):
    # Initialize the minimal signed binary string with the corresponding sign
    minimal_signed_binary_str = '+' if n > 0 else '-' if n < 0 else '0'
    # Iterate through the digits of the binary representation of n
    for i in range(len(bin(n)[2:])):
        # If the current digit is not zero, append the corresponding sign to the minimal signed binary string
        if bin(n)[2:][i] != '0':
            minimal_signed_binary_str += '+' if bin(n)[2:][i] == '1' else '-'
    return minimal_signed_binary_str

def main():
    n = int(input())
    print(get_minimal_signed_binary(n))

if __name__ == '__main__':
    main()

