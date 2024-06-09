
def get_quick_changes(routines):
    # Initialize a set to store the dancers who need a quick change
    quick_changes = set()
    
    # Iterate over the routines
    for i in range(len(routines)):
        # Get the dancers in the current routine
        dancers = routines[i]
        
        # Check if the dancers need a quick change
        if i > 0 and dancers[0] in quick_changes:
            # Add the dancers to the set of quick changes
            quick_changes.update(dancers)
    
    # Return the number of quick changes needed
    return len(quick_changes)

def main():
    # Read the number of routines
    num_routines = int(input())
    
    # Read the routines
    routines = []
    for i in range(num_routines):
        routines.append(input())
    
    # Get the minimum number of quick changes needed
    quick_changes = get_quick_changes(routines)
    
    # Print the result
    print(quick_changes)

if __name__ == '__main__':
    main()

