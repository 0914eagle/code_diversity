
def climb_pine(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate through each grasshopper and calculate the reachable branches
    for i in range(2, p + 1):
        for j in range(i, int(y / i) + 1):
            reachable_branches.append(j * i)

    # Sort and remove duplicates from the list of reachable branches
    reachable_branches = sorted(set(reachable_branches))

    # Check if the highest branch is reachable
    if y in reachable_branches:
        return -1
    else:
        # Return the highest branch that is not reachable
        return max(reachable_branches) + 1

