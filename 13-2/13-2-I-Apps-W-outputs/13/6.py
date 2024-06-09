
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
    enemies.sort(key=lambda x: x[0])

    # Iterate through the names and enemies lists
    for i in range(n):
        # Check if the current name is an enemy of the previous name
        if i > 0 and enemies[i-1][1] == names[i]:
            # If the current name is an enemy of the previous name, increment the current group size
            current_group_size += 1
        # Check if the current group size is greater than the capacity of the bus
        elif current_group_size > c:
            # If the current group size is greater than the capacity of the bus, increment the current number of groups
            current_groups += 1
            # Reset the current group size to 0
            current_group_size = 0
        # Add the current name to the current group
        groups[current_groups] = groups.get(current_groups, []) + [names[i]]

    # Return the minimum number of groups and the groups dictionary
    return min_groups, groups

