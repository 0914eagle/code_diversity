
def get_max_executives(num_briefcases, briefcase_contents):
    # Sort the briefcase contents in non-decreasing order
    briefcase_contents.sort()
    # Initialize the number of executives to be rewarded as 0
    num_executives = 0
    # Loop through the briefcase contents in reverse order
    for i in range(len(briefcase_contents) - 1, -1, -1):
        # If the current briefcase contains at least 1 banana, assign it to the current executive
        if briefcase_contents[i] >= 1:
            num_executives += 1
    # Return the maximum number of executives that can be rewarded
    return num_executives

