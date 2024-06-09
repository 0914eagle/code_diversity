
def f1(N):
    # Convert the binary string to an integer
    N = int(N, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible values of the most significant bit
    for i in range(3):
        # Calculate the current representation
        representation = N - i * 2**(len(N.bit_length()) - 1)
        
        # Add the representation to the set
        representations.add(representation)
    
    # Return the number of different representations
    return len(representations) % 1000000009

def f2(N):
    # Convert the binary string to an integer
    N = int(N, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible values of the most significant bit
    for i in range(3):
        # Calculate the current representation
        representation = N - i * 2**(len(N.bit_length()) - 1)
        
        # Add the representation to the set
        representations.add(representation)
    
    # Return the number of different representations
    return len(representations) % 1000000009

if __name__ == '__main__':
    N = input()
    print(f1(N))

