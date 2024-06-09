
def solve(n, k, c, names, enemies):
    # Initialize the minimum number of groups to n
    min_groups = n
    # Initialize the current number of groups to 0
    current_groups = 0
    # Initialize the current group size to 0
    current_group_size = 0
    # Initialize the groups dictionary to store the groups
    groups = {}

    # Sort the names and enemies lists
    names.sort()
    enemies.sort(key=lambda x: (x[0], x[1]))

    # Iterate through the names and enemies lists
    for i in range(n):
        # If the current group size is less than the capacity of the bus, add the current name to the current group
        if current_group_size < c:
            current_group_size += 1
            groups[current_groups] = groups.get(current_groups, []) + [names[i]]
        # If the current group size is equal to the capacity of the bus, create a new group and add the current name to it
        else:
            current_groups += 1
            current_group_size = 1
            groups[current_groups] = [names[i]]

        # If the current name is an enemy of the previous name, create a new group and add both names to it
        if i > 0 and (names[i], names[i-1]) in enemies:
            current_groups += 1
            current_group_size = 2
            groups[current_groups] = [names[i], names[i-1]]

    # Return the minimum number of groups and the groups dictionary
    return min_groups, groups

