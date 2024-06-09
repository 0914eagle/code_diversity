
def min_quick_changes(routines):
    # Initialize a dictionary to keep track of the dancers and their quick change status
    dancers = {}
    for routine in routines:
        for dancer in routine:
            if dancer not in dancers:
                dancers[dancer] = "normal"
            elif dancers[dancer] == "normal":
                dancers[dancer] = "quick"
    
    # Count the number of quick changes needed
    quick_changes = 0
    for dancer, status in dancers.items():
        if status == "quick":
            quick_changes += 1
    
    return quick_changes

