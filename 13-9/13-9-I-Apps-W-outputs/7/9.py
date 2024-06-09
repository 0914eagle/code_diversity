
def get_highest_branch(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate from 2 to y
    for x in range(2, y + 1):
        # Check if x is a factor of y
        if y % x == 0:
            # Add the reachable branch to the list
            reachable_branches.append(x)

    # Check if there are any reachable branches
    if not reachable_branches:
        # Return -1 if there are no reachable branches
        return -1

    # Sort the reachable branches in descending order
    reachable_branches.sort(reverse=True)

    # Return the highest reachable branch
    return reachable_branches[0]

