
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
        # Check if the current name is an enemy of the previous name
        if i > 0 and (names[i], names[i-1]) in enemies:
            # If the current name is an enemy of the previous name, increment the current group size
            current_group_size += 1
        else:
            # If the current name is not an enemy of the previous name, add the current group to the groups dictionary
            groups[current_groups] = names[i-current_group_size:i]
            # Increment the current group size
            current_group_size = 1
            # Increment the current number of groups
            current_groups += 1

    # Add the last group to the groups dictionary
    groups[current_groups] = names[n-current_group_size:]

    # Initialize the final groups list
    final_groups = []

    # Iterate through the groups dictionary
    for group in groups.values():
        # Check if the current group size is less than or equal to the bus capacity
        if len(group) <= c:
            # If the current group size is less than or equal to the bus capacity, add the current group to the final groups list
            final_groups.append(group)
        else:
            # If the current group size is greater than the bus capacity, split the current group into multiple groups
            for i in range(0, len(group), c):
                # Add the current group to the final groups list
                final_groups.append(group[i:i+c])

    # Return the minimum number of groups and the final groups list
    return min_groups, final_groups

