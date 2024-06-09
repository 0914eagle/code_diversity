
def get_highest_branch(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate over the first p branches
    for i in range(2, p + 1):
        # Get the reachable branches for the current branch
        reachable_branches += [i * j for j in range(1, int(y / i) + 1)]

    # Sort and remove duplicates
    reachable_branches = sorted(set(reachable_branches))

    # Check if the highest branch is reachable
    if y in reachable_branches:
        return -1
    else:
        # Return the highest branch that is not reachable
        return max(reachable_branches) + 1

