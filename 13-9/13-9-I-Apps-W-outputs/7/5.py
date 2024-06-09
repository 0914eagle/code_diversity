
def solve(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate through each grasshopper and add the reachable branches to the list
    for i in range(2, p + 1):
        for j in range(i, int(y / i) + 1):
            reachable_branches.append(j * i)

    # Sort the list in ascending order
    reachable_branches.sort()

    # Check if the highest branch is reachable
    if y in reachable_branches:
        return -1
    else:
        # Return the highest branch that is not reachable
        return y

