
def get_signatures(k, desks):
    # Sort the desks in ascending order
    desks.sort()
    
    # Initialize the current desk number to 1
    current_desk = 1
    
    # Initialize the number of passes to 0
    passes = 0
    
    # Loop through each desk number
    for desk in desks:
        # If the current desk number is less than the desk number we need to sign, we need to pass through the line
        if current_desk < desk:
            passes += 1
        # If the current desk number is greater than the desk number we need to sign, we need to back up and pass through the line again
        elif current_desk > desk:
            passes += 1
            current_desk = desk
        # If the current desk number is equal to the desk number we need to sign, we can move on to the next desk
        else:
            current_desk += 1
    
    # Return the number of passes needed
    return passes

