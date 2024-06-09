
def get_max_executives(briefcases):
    # Sort the briefcases by the number of bananas in each briefcase
    sorted_briefcases = sorted(briefcases, key=lambda x: x[1])

    # Initialize the maximum number of executives to be rewarded
    max_executives = 0

    # Initialize the number of executives to be rewarded
    num_executives = 0

    # Initialize the total number of bananas to be rewarded
    total_bananas = 0

    # Loop through the sorted briefcases
    for briefcase in sorted_briefcases:
        # If the total number of bananas to be rewarded plus the number of bananas in the current briefcase is less than or equal to the number of bananas in the previous briefcase,
        # then the current executive is not the most evil executive
        if total_bananas + briefcase[1] <= sorted_briefcases[num_executives - 1][1]:
            # Increment the number of executives to be rewarded
            num_executives += 1
            # Add the number of bananas in the current briefcase to the total number of bananas to be rewarded
            total_bananas += briefcase[1]
        # Otherwise, the current executive is the most evil executive
        else:
            # Break out of the loop
            break

    # Return the maximum number of executives to be rewarded
    return num_executives

