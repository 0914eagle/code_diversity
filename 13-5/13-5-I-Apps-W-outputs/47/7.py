
def get_min_quick_changes(routines):
    # Initialize a set to store the dancers who require a quick change
    quick_change_dancers = set()
    # Iterate through the routines
    for i in range(len(routines)):
        # Get the dancers for the current routine
        dancers = routines[i]
        # Check if the dancers require a quick change
        if i > 0 and set(dancers) & quick_change_dancers:
            # If they do, add them to the set of dancers who require a quick change
            quick_change_dancers |= set(dancers)
    # Return the number of quick changes required
    return len(quick_change_dancers)

