
def get_max_executives(num_briefcases, briefcase_contents):
    # Sort the briefcase contents in non-decreasing order
    sorted_briefcases = sorted(briefcase_contents)

    # Initialize the number of executives to be rewarded
    num_executives = 0

    # Loop through the sorted briefcases and assign them to the executives
    for i in range(len(sorted_briefcases)):
        # If the current briefcase is not empty, assign it to the current executive
        if sorted_briefcases[i] > 0:
            num_executives += 1

    return num_executives

