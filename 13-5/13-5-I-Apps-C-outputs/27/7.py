
def f1(N):
    # Convert the binary string to an integer
    N = int(N, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible representations of N
    for i in range(N+1):
        # Convert the current representation to binary
        representation = bin(i)[2:]
        
        # Check if the representation contains only 0 and 1
        if all(c in "01" for c in representation):
            # Add the representation to the set
            representations.add(representation)
    
    # Return the number of different representations
    return len(representations)

def f2(N):
    # Convert the binary string to an integer
    N = int(N, 2)
    
    # Initialize a set to store the different representations
    representations = set()
    
    # Iterate through all possible representations of N
    for i in range(N+1):
        # Convert the current representation to binary
        representation = bin(i)[2:]
        
        # Check if the representation contains only 0 and 1
        if all(c in "01" for c in representation):
            # Add the representation to the set
            representations.add(representation)
    
    # Return the number of different representations
    return len(representations)

if __name__ == '__main__':
    N = input()
    print(f1(N) % 1000000009)

