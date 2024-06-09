
def get_binary_representations(binary_string):
    # Initialize a list to store the binary representations
    representations = []
    
    # Loop through each character in the binary string
    for i in range(len(binary_string)):
        # Get the current character
        char = binary_string[i]
        
        # If the current character is '2', add it to the representation
        if char == '2':
            representations.append(binary_string[:i] + '2' + binary_string[i+1:])
    
    # Return the number of representations
    return len(representations)

def main():
    # Read a line of input from stdin and convert it to an integer
    n = int(input().strip())
    
    # Convert the integer to a binary string
    binary_string = bin(n)[2:]
    
    # Call the function to get the number of binary representations
    num_representations = get_binary_representations(binary_string)
    
    # Print the number of representations modulo 1000000009
    print(num_representations % 1000000009)

if __name__ == '__main__':
    main()

