
def get_max_executives(num_briefcases, briefcase_contents):
    # Sort the briefcase contents in non-decreasing order
    briefcase_contents.sort()
    # Initialize the number of executives to be rewarded as 0
    num_executives = 0
    # Loop through the briefcase contents and award briefcases to executives
    for i in range(len(briefcase_contents)):
        # If the current briefcase content is greater than or equal to the previous content, award the briefcase to the current executive
        if i == 0 or briefcase_contents[i] >= briefcase_contents[i-1]:
            num_executives += 1
    # Return the maximum number of executives that can be rewarded
    return num_executives

