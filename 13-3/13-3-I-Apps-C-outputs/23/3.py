
def get_max_executives(briefcases):
    # Sort the briefcases by the number of bananas in each briefcase
    sorted_briefcases = sorted(briefcases, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of executives and the total number of bananas
    num_executives = 0
    total_bananas = 0

    # Loop through the sorted briefcases and assign them to the executives
    for briefcase in sorted_briefcases:
        # If the total number of bananas is less than the number of executives, give the briefcase to the current executive
        if total_bananas < num_executives:
            total_bananas += briefcase[1]
        # Otherwise, give the briefcase to the next executive
        else:
            num_executives += 1
            total_bananas = briefcase[1]

    return num_executives

