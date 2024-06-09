
def get_permits(k, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()
    
    # Initialize the number of passes as 0
    num_passes = 0
    
    # Loop through each desk number
    for i in range(len(desk_numbers)):
        # If the desk number is not equal to the current pass number, we need to move forward
        if desk_numbers[i] != i + 1:
            # Increment the number of passes by 1
            num_passes += 1
    
    # Return the number of passes
    return num_passes

