
def solve(received_string, remembered_substring):
    # Initialize a list to store all possible values of n
    n_list = []
    
    # Loop through all possible values of n
    for i in range(1000000):
        # Convert the current value of n to a string
        n_str = str(i)
        
        # Check if the current value of n has the correct number of digits
        if len(n_str) == len(received_string):
            # Check if the current value of n has the correct substring
            if n_str.endswith(remembered_substring):
                # Add the current value of n to the list
                n_list.append(i)
    
    # Sort the list of possible values of n in ascending order
    n_list.sort()
    
    # Return the smallest possible value of n
    return n_list[0]

