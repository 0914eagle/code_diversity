
def get_signatures(num_signatures, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()
    
    # Initialize a variable to keep track of the number of passes
    num_passes = 0
    
    # Loop through each desk number and check if it is in the correct position
    for i in range(len(desk_numbers)):
        if desk_numbers[i] != i + 1:
            num_passes += 1
    
    return num_passes

