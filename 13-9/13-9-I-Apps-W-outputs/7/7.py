
def get_highest_branch(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate through each grasshopper and add their reachable branches to the list
    for i in range(2, p + 1):
        for j in range(i, int(y / i) + 1):
            reachable_branches.append(j * i)

    # Sort the list in ascending order
    reachable_branches.sort()

    # Check if the highest branch is reachable
    if reachable_branches[-1] == y:
        return -1
    else:
        return y

