
def solve(n, k, c, names, enemies):
    # Initialize the minimum number of groups to n
    min_groups = n
    # Initialize the current number of groups to 0
    current_groups = 0
    # Initialize the current group size to 0
    current_group_size = 0
    # Initialize the groups list
    groups = []

    # Sort the names and enemies lists
    names.sort()
    enemies.sort(key=lambda x: (x[0], x[1]))

    # Iterate through the names list
    for name in names:
        # Check if the current group size is less than the capacity of the bus
        if current_group_size < c:
            # Add the name to the current group
            current_group_size += 1
            groups[-1].append(name)
        # If the current group size is greater than or equal to the capacity of the bus
        else:
            # Increment the current number of groups
            current_groups += 1
            # Create a new group with the current name
            groups.append([name])
            # Reset the current group size
            current_group_size = 1

    # If the current group size is less than the capacity of the bus
    if current_group_size < c:
        # Add the current group to the groups list
        groups.append(groups[-1])

    # Return the minimum number of groups and the groups list
    return min_groups, groups

