
def solve(n, k, c, names, enemies):
    # Initialize variables
    groups = []
    current_group = []
    group_size = 0

    # Sort the names and enemies by the number of enemies each kid has
    sorted_names = sorted(names, key=lambda x: len(enemies[x]))

    # Iterate through the sorted names
    for name in sorted_names:
        # If the current group is full, create a new group
        if group_size == c:
            groups.append(current_group)
            current_group = []
            group_size = 0

        # If the name is not an enemy of anyone in the current group, add it to the group
        if all(name not in group for group in current_group):
            current_group.append(name)
            group_size += 1

    # Add the last group if it is not empty
    if current_group:
        groups.append(current_group)

    return groups

