
def solve(routines):
    # Initialize a dictionary to keep track of the dancers and their costume changes
    dancers = {}
    for routine in routines:
        for dancer in routine:
            if dancer not in dancers:
                dancers[dancer] = 0
            dancers[dancer] += 1

    # Initialize a variable to keep track of the total number of quick changes
    quick_changes = 0

    # Iterate through the dancers and their costume changes
    for dancer, changes in dancers.items():
        if changes > 1:
            quick_changes += changes - 1

    return quick_changes

