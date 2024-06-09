
def get_signatures(k, desk_numbers):
    # Initialize a list to store the desk numbers in ascending order
    desk_numbers_sorted = sorted(desk_numbers)
    
    # Initialize a variable to store the number of passes needed
    num_passes = 0
    
    # Loop through the desk numbers in ascending order
    for i in range(len(desk_numbers_sorted)):
        # If the current desk number is not equal to the current index + 1,
        # it means that the signatures above the current clerk's name have not been filled in yet
        if desk_numbers_sorted[i] != i + 1:
            # Increment the number of passes needed
            num_passes += 1
    
    # Return the number of passes needed
    return num_passes

