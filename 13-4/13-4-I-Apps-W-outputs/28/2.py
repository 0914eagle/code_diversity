
def get_quick_changes(routines):
    # Initialize a set to store the dancers who have performed
    performed_dancers = set()
    # Initialize a counter for the quick changes
    quick_changes = 0
    # Iterate through the routines
    for routine in routines:
        # Iterate through the dancers in the current routine
        for dancer in routine:
            # If the dancer has performed before, increment the quick changes
            if dancer in performed_dancers:
                quick_changes += 1
            # Add the dancer to the set of performed dancers
            performed_dancers.add(dancer)
    return quick_changes

def main():
    # Read the number of routines
    num_routines = int(input())
    # Read the routines
    routines = []
    for _ in range(num_routines):
        routines.append(input())
    # Get the minimum number of quick changes
    quick_changes = get_quick_changes(routines)
    # Print the result
    print(quick_changes)

if __name__ == '__main__':
    main()

