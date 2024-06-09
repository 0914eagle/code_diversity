
def get_signatures(k, desks):
    # Sort the desks in increasing order
    desks.sort()
    
    # Initialize the number of passes as 0
    num_passes = 0
    
    # Loop through each desk and check if it is in the correct order
    for i in range(len(desks)):
        if desks[i] != i + 1:
            # If a desk is not in the correct order, increase the number of passes by 1
            num_passes += 1
    
    # Return the number of passes needed
    return num_passes

