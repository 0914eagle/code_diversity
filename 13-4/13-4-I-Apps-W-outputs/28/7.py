
def get_quick_changes(routines):
    # Initialize a set to store the dancers who have performed
    performed_dancers = set()
    # Initialize a counter for the quick changes
    quick_changes = 0
    # Iterate through the routines
    for routine in routines:
        # Get the dancers in the current routine
        dancers = set(routine)
        # Check if any dancers in the current routine have performed before
        if len(performed_dancers.intersection(dancers)) > 0:
            # If so, increment the quick changes counter
            quick_changes += 1
        # Add the dancers in the current routine to the performed dancers set
        performed_dancers.update(dancers)
    # Return the quick changes counter
    return quick_changes

def main():
    # Read the number of routines
    num_routines = int(input())
    # Read the routines
    routines = []
    for _ in range(num_routines):
        routines.append(input())
    # Get the quick changes
    quick_changes = get_quick_changes(routines)
    # Print the quick changes
    print(quick_changes)

if __name__ == '__main__':
    main()

