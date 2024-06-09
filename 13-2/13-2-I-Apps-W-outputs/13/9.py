
def solve(n, k, c, names, enemies):
    # Initialize variables
    groups = []
    current_group = []
    group_size = 0
    i = 0

    # Iterate through the names
    while i < n:
        # If the current group is full, create a new group
        if group_size == c:
            groups.append(current_group)
            current_group = []
            group_size = 0

        # If the current name is not an enemy of anyone in the current group, add it to the group
        if not any(name in current_group for name in enemies[names[i]]):
            current_group.append(names[i])
            group_size += 1

        # If the current name is an enemy of everyone in the current group, create a new group with only that name
        elif group_size > 0:
            groups.append(current_group)
            current_group = [names[i]]
            group_size = 1

        i += 1

    # Add the last group to the list of groups
    if current_group:
        groups.append(current_group)

    return len(groups), groups

