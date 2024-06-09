
def solve(received_string, remembered_substring):
    # Initialize a list to store all possible values of n
    n_list = []
    
    # Loop through all possible values of n
    for i in range(1000000):
        # Convert the current value of n to a string
        n_string = str(i)
        
        # Check if the current value of n has the same number of digits as the received string
        if len(n_string) == len(received_string):
            # Check if the current value of n has the same substring as the remembered substring
            if n_string.endswith(remembered_substring):
                # Add the current value of n to the list of possible values
                n_list.append(i)
    
    # Return the smallest value of n
    return min(n_list)

