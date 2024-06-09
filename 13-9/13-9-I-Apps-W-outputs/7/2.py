
def solve(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate through each grasshopper's jumping range
    for i in range(2, p + 1):
        # Get the jumping range for the current grasshopper
        jump_range = [i * j for j in range(1, int(y / i) + 1)]

        # Add the jumping range to the list of reachable branches
        reachable_branches += jump_range

    # Sort and remove duplicates from the list of reachable branches
    reachable_branches = sorted(set(reachable_branches))

    # Check if there are any unreachable branches
    for i in range(y, 1, -1):
        if i not in reachable_branches:
            return i

    # If all branches are reachable, return -1
    return -1

