
def get_signatures(num_signatures, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()
    
    # Initialize variables to keep track of the current desk number and the number of passes
    current_desk = 1
    num_passes = 0
    
    # Loop through each desk number and check if it is the next desk number in the line
    for desk in desk_numbers:
        while current_desk < desk:
            current_desk += 1
            num_passes += 1
        current_desk += 1
    
    # Return the number of passes needed to collect all the signatures
    return num_passes + 1

