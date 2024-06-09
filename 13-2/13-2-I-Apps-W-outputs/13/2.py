
def solve(n, k, c, names, enemies):
    # Initialize the minimum number of groups as 0
    min_groups = 0
    # Initialize the groups as an empty list
    groups = []
    # Loop through each name in the names list
    for name in names:
        # Check if the name is already in a group
        if name not in groups:
            # If the name is not in a group, add it to a new group
            groups.append([name])
            # Increment the minimum number of groups
            min_groups += 1
        # Loop through each enemy pair
        for enemy1, enemy2 in enemies:
            # Check if the name is an enemy of any other name in the group
            if name in groups and enemy1 in groups and enemy2 in groups:
                # If the name is an enemy of any other name in the group, merge the groups
                groups = merge_groups(groups, enemy1, enemy2)
                # Decrement the minimum number of groups
                min_groups -= 1
    # Return the minimum number of groups and the groups
    return min_groups, groups

def merge_groups(groups, name1, name2):
    # Find the index of the group that contains name1
    index1 = groups.index(name1)
    # Find the index of the group that contains name2
    index2 = groups.index(name2)
    # Merge the two groups into a new group
    new_group = groups[index1] + groups[index2]
    # Remove the old groups
    groups.pop(index1)
    groups.pop(index2-1)
    # Add the new group to the list of groups
    groups.append(new_group)
    # Return the updated list of groups
    return groups

# Main function
def main():
    # Read the input
    n, k, c = map(int, input().split())
    names = []
    enemies = []
    for i in range(n):
        names.append(input())
    for i in range(k):
        enemy1, enemy2 = input().split()
        enemies.append((enemy1, enemy2))
    # Call the solve function
    min_groups, groups = solve(n, k, c, names, enemies)
    # Print the minimum number of groups
    print(min_groups)
    # Print the groups
    for group in groups:
        print(" ".join(group))

if __name__ == "__main__":
    main()

