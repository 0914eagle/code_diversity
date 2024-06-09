
def get_permits(k, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()
    
    # Initialize the current desk number to 1
    current_desk = 1
    
    # Initialize the number of passes to 0
    num_passes = 0
    
    # Loop through each desk number
    for desk in desk_numbers:
        # If the current desk number is less than the desk number, we need to pass through the line
        if current_desk < desk:
            num_passes += 1
        
        # Update the current desk number
        current_desk = desk
    
    # Return the number of passes
    return num_passes

