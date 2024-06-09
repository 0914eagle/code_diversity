
def get_quick_changes(routines):
    # Initialize a set to store the dancers who need a quick change
    quick_changes = set()
    
    # Iterate through the routines
    for i in range(len(routines)):
        # Get the dancers in the current routine
        dancers = routines[i]
        
        # Check if the dancers in the current routine are already in the set of dancers who need a quick change
        if any(dancer in quick_changes for dancer in dancers):
            # If they are, add them to the set of dancers who need a quick change
            quick_changes.update(dancers)
    
    # Return the number of quick changes needed
    return len(quick_changes)

def main():
    # Read the number of routines
    num_routines = int(input())
    
    # Read the routines
    routines = []
    for _ in range(num_routines):
        routines.append(input())
    
    # Get the minimum number of quick changes needed
    quick_changes = get_quick_changes(routines)
    
    # Print the result
    print(quick_changes)

if __name__ == '__main__':
    main()

