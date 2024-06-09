
def get_max_executives(briefcases):
    # Sort the briefcases by the number of bananas in each briefcase
    sorted_briefcases = sorted(briefcases, key=lambda x: x[1])

    # Initialize the maximum number of executives to be rewarded
    max_executives = 0

    # Initialize the number of executives to be rewarded
    num_executives = 0

    # Initialize the total number of bananas to be distributed
    total_bananas = sum(briefcase[1] for briefcase in briefcases)

    # Loop through the sorted briefcases
    for briefcase in sorted_briefcases:
        # If the total number of bananas to be distributed is less than the number of executives to be rewarded, break the loop
        if total_bananas < num_executives:
            break

        # Add the number of bananas in the current briefcase to the total number of bananas to be distributed
        total_bananas += briefcase[1]

        # Increment the number of executives to be rewarded
        num_executives += 1

    # Return the maximum number of executives that can be rewarded
    return num_executives

