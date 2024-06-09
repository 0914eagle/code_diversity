
def get_signatures(num_signatures, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()
    
    # Initialize a variable to keep track of the number of passes
    num_passes = 0
    
    # Loop through each desk number
    for i in range(len(desk_numbers)):
        # If the desk number is greater than the current pass number, we need to make another pass
        if desk_numbers[i] > num_passes:
            num_passes = desk_numbers[i]
    
    # Return the number of passes needed
    return num_passes

