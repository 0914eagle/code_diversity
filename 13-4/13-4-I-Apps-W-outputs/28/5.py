
def get_quick_changes(routines):
    # Initialize a set to store the dancers who need a quick change
    quick_changes = set()
    
    # Iterate over the routines
    for i in range(len(routines)):
        # Get the dancers in the current routine
        dancers = routines[i]
        
        # Check if the dancers are already in the set of quick changes
        if any(dancer in quick_changes for dancer in dancers):
            # If they are, add them to the set of quick changes
            quick_changes.update(dancers)
    
    # Return the number of quick changes needed
    return len(quick_changes)

def main():
    # Read the number of routines
    num_routines = int(input())
    
    # Initialize an empty list to store the routines
    routines = []
    
    # Iterate over the number of routines
    for _ in range(num_routines):
        # Read the routine
        routine = input()
        
        # Add the routine to the list of routines
        routines.append(routine)
    
    # Get the number of quick changes needed
    quick_changes = get_quick_changes(routines)
    
    # Print the number of quick changes needed
    print(quick_changes)

if __name__ == '__main__':
    main()

