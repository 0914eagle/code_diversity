
def highest_branch(p, y):
    # Initialize a list to store the reachable branches
    reachable_branches = []

    # Iterate from 2 to y
    for x in range(2, y + 1):
        # Check if the current branch is occupied by a grasshopper
        if x <= p:
            # If the current branch is occupied, add it to the list of reachable branches
            reachable_branches.append(x)
        else:
            # If the current branch is not occupied, check if it can be reached by any of the grasshoppers
            for i in range(2, int(y / x) + 1):
                if x * i <= y:
                    reachable_branches.append(x * i)

    # Sort the list of reachable branches in descending order
    reachable_branches.sort(reverse=True)

    # Check if there are any valid branches
    if len(reachable_branches) == 0:
        return -1
    else:
        # Return the highest valid branch
        return reachable_branches[0]

