
def get_signatures(num_signatures, desk_numbers):
    # Sort the desk numbers in ascending order
    desk_numbers.sort()

    # Initialize a variable to keep track of the number of passes
    num_passes = 0

    # Loop through each desk number and check if it is the current desk number
    for i in range(1, max(desk_numbers) + 1):
        if i in desk_numbers:
            # If the current desk number is in the list of desk numbers, increment the number of passes
            num_passes += 1

    # Return the number of passes
    return num_passes

