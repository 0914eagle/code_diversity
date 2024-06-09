
def solve(received_string, remembered_substring):
    # Initialize a list to store all possible values of n
    n_list = []
    
    # Loop through all possible values of n
    for i in range(1000000):
        # Convert the current value of n to a string
        n_str = str(i)
        
        # Check if the current value of n has the same number of digits as the received string
        if len(n_str) == len(received_string):
            # Check if the current value of n has the same digits as the received string
            if n_str == received_string:
                # If the current value of n has the same digits as the received string, add it to the list of possible values of n
                n_list.append(i)
    
    # Initialize a variable to store the smallest possible value of n
    smallest_n = 0
    
    # Loop through all possible values of n
    for n in n_list:
        # Convert the current value of n to a string
        n_str = str(n)
        
        # Check if the current value of n has the same digits as the remembered substring
        if n_str == remembered_substring:
            # If the current value of n has the same digits as the remembered substring, update the smallest possible value of n
            smallest_n = n
    
    # Return the smallest possible value of n
    return smallest_n

