
def solve(n, k, c, names, enemies):
    # Initialize the minimum number of groups as 0
    min_groups = 0
    # Initialize the groups as an empty list
    groups = []
    # Loop through each name in the names list
    for name in names:
        # Check if the name is already in a group
        if name not in groups:
            # If not, add the name to a new group
            groups.append([name])
            # Increment the minimum number of groups
            min_groups += 1
        # Loop through each enemy pair
        for enemy1, enemy2 in enemies:
            # Check if the name is an enemy of any other name in the group
            if name in groups and enemy1 in groups and enemy2 in groups:
                # If so, merge the two groups into a single group
                groups[groups.index(enemy1)] += groups[groups.index(enemy2)]
                # Remove the merged group from the list of groups
                groups.remove(groups[groups.index(enemy2)])
                # Decrement the minimum number of groups
                min_groups -= 1
    # Return the minimum number of groups and the groups list
    return min_groups, groups

