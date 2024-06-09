
def get_binary_representations(N):
    # Initialize a list to store the binary representations
    representations = []
    
    # Iterate through all possible binary representations of N
    for i in range(N+1):
        # Convert the current representation to a string
        representation = bin(i)[2:]
        
        # Check if the representation contains the digit 2
        if '2' in representation:
            # Add the representation to the list
            representations.append(representation)
    
    # Return the number of representations that contain the digit 2
    return len(representations)

def get_remainder(N):
    # Calculate the number of binary representations of N that contain the digit 2
    representations = get_binary_representations(N)
    
    # Calculate the remainder modulo 1000000009
    remainder = representations % 1000000009
    
    # Return the remainder
    return remainder

if __name__ == '__main__':
    # Read a line of input from stdin and convert it to an integer
    N = int(input().strip())
    
    # Call the function to get the number of binary representations of N that contain the digit 2
    result = get_remainder(N)
    
    # Print the result
    print(result)

