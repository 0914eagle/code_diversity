
def get_binary_representations(binary_string):
    # Initialize a list to store the binary representations
    representations = []
    
    # Iterate through the binary string
    for i in range(len(binary_string)):
        # Get the current digit
        digit = binary_string[i]
        
        # If the digit is 2, add it to the representations list
        if digit == "2":
            representations.append(digit)
    
    # Return the number of representations
    return len(representations)

def get_binary_representations_modulo(binary_string):
    # Get the number of binary representations
    representations = get_binary_representations(binary_string)
    
    # Return the number of representations modulo 1000000009
    return representations % 1000000009

if __name__ == '__main__':
    # Read a line of input from stdin and convert it to an integer
    n = int(input().strip())
    
    # Convert the integer to a binary string
    binary_string = bin(n)[2:]
    
    # Call the function to get the number of binary representations modulo 1000000009
    result = get_binary_representations_modulo(binary_string)
    
    # Print the result
    print(result)

