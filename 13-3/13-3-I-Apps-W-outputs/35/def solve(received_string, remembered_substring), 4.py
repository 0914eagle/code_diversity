
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
    
    # Sort the set of possible values in ascending order
    possible_n = sorted(possible_n)
    
    # Return the smallest value in the set
    return possible_n[0]

