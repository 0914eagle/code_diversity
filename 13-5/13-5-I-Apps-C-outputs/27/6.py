
def f1(binary_string):
    # Convert the binary string to an integer
    n = int(binary_string, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible values of the last digit
    for last_digit in range(3):
        # Calculate the current representation
        representation = n + last_digit
        
        # Add the representation to the set
        representations.add(representation)
    
    # Return the number of different representations
    return len(representations)

def f2(binary_string):
    # Convert the binary string to an integer
    n = int(binary_string, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible values of the last digit
    for last_digit in range(3):
        # Calculate the current representation
        representation = n + last_digit
        
        # Add the representation to the set
        representations.add(representation)
    
    # Return the number of different representations
    return len(representations) % 1000000009

if __name__ == '__main__':
    binary_string = input()
    print(f1(binary_string))
    print(f2(binary_string))

