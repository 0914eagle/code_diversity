
def solve(received_string, remembered_substring):
    # Initialize a set to store the possible values of n
    possible_n = set()
    
    # Iterate through all possible values of n
    for n in range(1000000):
        # Convert n to a string
        n_str = str(n)
        
        # Check if the substring is a substring of n_str
        if remembered_substring in n_str:
            # Add n to the set of possible values
            possible_n.add(n)
    
    # Initialize the smallest possible value of n as the largest possible value
    smallest_n = 1000000
    
    # Iterate through the set of possible values
    for n in possible_n:
        # Convert n to a string
        n_str = str(n)
        
        # Check if the substring is a substring of n_str
        if remembered_substring in n_str:
            # Check if the length of n_str is less than the length of the received string
            if len(n_str) < len(received_string):
                # Add the length of n_str to the smallest possible value of n
                smallest_n = min(smallest_n, len(n_str))
    
    # Return the smallest possible value of n
    return smallest_n

