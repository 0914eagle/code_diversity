
def solve(n, k, c, names, enemies):
    # Initialize variables
    groups = []
    current_group = []
    group_size = 0
    i = 0

    # Iterate through the names
    while i < n:
        # If the current group is full, add it to the list of groups and create a new group
        if group_size == c:
            groups.append(current_group)
            current_group = []
            group_size = 0

        # If the current name is not an enemy of anyone in the current group, add it to the group
        if not any(name in current_group for name in enemies[i]):
            current_group.append(names[i])
            group_size += 1

        # If the current name is an enemy of everyone in the current group, create a new group with only that name
        elif all(name in current_group for name in enemies[i]):
            groups.append([names[i]])

        # Increment the index
        i += 1

    # Add the last group to the list of groups
    if current_group:
        groups.append(current_group)

    # Return the minimum number of groups and the list of groups
    return len(groups), groups

