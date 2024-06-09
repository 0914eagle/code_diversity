
def min_quick_changes(routines):
    # Initialize a dictionary to keep track of the dancers and their quick change status
    dancers = {}
    for routine in routines:
        for dancer in routine:
            if dancer not in dancers:
                dancers[dancer] = False
            if routine[0] != dancer:
                dancers[dancer] = True
    
    # Count the number of quick changes needed
    quick_changes = 0
    for dancer, needs_quick_change in dancers.items():
        if needs_quick_change:
            quick_changes += 1
    
    return quick_changes

