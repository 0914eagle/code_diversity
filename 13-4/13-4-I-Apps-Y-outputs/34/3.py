
def get_number_of_passes(k, desk_numbers):
    # Initialize a dictionary to keep track of the desk numbers and their corresponding signatures
    desk_signatures = {}
    for desk_number in desk_numbers:
        desk_signatures[desk_number] = 0

    # Initialize the number of passes to 0
    num_passes = 0

    # Loop through the desk numbers and increment the number of passes for each desk number
    for desk_number in desk_numbers:
        if desk_number not in desk_signatures:
            num_passes += 1
        else:
            desk_signatures[desk_number] += 1

    # Return the number of passes
    return num_passes

