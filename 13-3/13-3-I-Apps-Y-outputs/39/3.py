
def get_minimum_inspectors(n, d):
    # Initialize a list to store the inspectors
    inspectors = []

    # Loop through each tree
    for i in range(1, n + 1):
        # Check if the tree is within the range of the current inspector
        if i >= len(inspectors) or i < inspectors[len(inspectors) - 1] - d or i > inspectors[len(inspectors) - 1] + d:
            # If not, add a new inspector
            inspectors.append(i)

    # Return the number of inspectors needed
    return len(inspectors)

