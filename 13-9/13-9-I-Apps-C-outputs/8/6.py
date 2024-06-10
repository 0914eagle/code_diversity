
def find_signed_binary_representation(n):
    # Initialize an empty list to store the signed binary representation
    sb_representation = []
    
    # Convert the input number to binary
    binary_representation = bin(n)[2:]
    
    # Iterate through the binary representation
    for digit in binary_representation:
        # If the digit is 0, append a 0 to the signed binary representation
        if digit == "0":
            sb_representation.append("0")
        # If the digit is 1, append a +1 to the signed binary representation
        elif digit == "1":
            sb_representation.append("+")
    
    # Return the signed binary representation
    return "".join(sb_representation)

def main():
    # Take input from the user
    n = int(input())
    
    # Find the signed binary representation of the input number
    sb_representation = find_signed_binary_representation(n)
    
    # Print the signed binary representation
    print(sb_representation)

if __name__ == '__main__':
    main()

