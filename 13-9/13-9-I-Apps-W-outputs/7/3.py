
def get_highest_branch(p, y):
    # Initialize a list to store the positions of the grasshoppers
    grasshoppers = []

    # Add the positions of the first p grasshoppers to the list
    for i in range(2, p+1):
        grasshoppers.append(i)

    # Iterate through the remaining branches and check if they can be reached by any of the grasshoppers
    for i in range(p+1, y+1):
        # If the current branch is not reachable by any of the grasshoppers, return it as the highest suitable branch
        if i not in grasshoppers:
            return i

        # If the current branch is reachable by some grasshopper, add its jumping distance to the list of positions
        for j in range(len(grasshoppers)):
            if i % grasshoppers[j] == 0:
                grasshoppers.append(i)
                break

    # If no suitable branch is found, return -1
    return -1

