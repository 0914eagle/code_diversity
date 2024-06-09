
def get_permits(num_permits, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()

    # Initialize variables to keep track of the number of passes and current desk number
    num_passes = 0
    current_desk = 1

    # Loop through each desk number and check if it is the current desk number
    for desk in desk_numbers:
        if desk == current_desk:
            # If the desk number matches the current desk number, increment the current desk number and number of passes
            current_desk += 1
            num_passes += 1
        else:
            # If the desk number does not match the current desk number, increment the number of passes only
            num_passes += 1

    # Return the number of passes
    return num_passes

