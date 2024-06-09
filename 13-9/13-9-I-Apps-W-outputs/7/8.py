
def find_highest_branch(p, y):
    # Initialize a list to store the positions of the grasshoppers
    grasshoppers = []
    # Iterate from 2 to y
    for i in range(2, y + 1):
        # If the current position is not a multiple of p, it means that a grasshopper is present
        if i % p != 0:
            grasshoppers.append(i)
    # Sort the list of grasshoppers in ascending order
    grasshoppers.sort()
    # Initialize a variable to store the highest suitable branch
    highest_branch = -1
    # Iterate through the list of grasshoppers
    for i in range(len(grasshoppers)):
        # If the current branch is not reachable by any of the grasshoppers, it is a suitable branch
        if grasshoppers[i] > highest_branch:
            highest_branch = grasshoppers[i]
    # Return the highest suitable branch
    return highest_branch

