
def get_signatures(num_signatures, clerk_desks):
    # Sort the clerk desks in ascending order
    clerk_desks.sort()
    
    # Initialize the current desk number to 1
    current_desk = 1
    
    # Initialize the number of passes to 0
    num_passes = 0
    
    # Loop through each clerk desk
    for desk in clerk_desks:
        # If the current desk number is less than the clerk desk, we need to pass through the line
        if current_desk < desk:
            num_passes += 1
        # Update the current desk number to the next desk
        current_desk = desk + 1
    
    # Return the number of passes needed
    return num_passes

