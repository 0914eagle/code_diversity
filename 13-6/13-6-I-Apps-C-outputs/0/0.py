
def f1(n, m, t, op):
    # Initialize a dictionary to store the valid assignments for each grid square
    valid_assignments = {}
    
    # Initialize a set to store the used numbers
    used_numbers = set()
    
    # Iterate over the grid locations
    for i in range(m):
        # Read the row and column number for the current grid location
        r, c = map(int, input().split())
        
        # Check if the current grid location is already used
        if (r, c) in valid_assignments:
            # If the current grid location is already used, return 0
            return 0
        
        # Add the current grid location to the valid assignments dictionary
        valid_assignments[(r, c)] = set()
        
        # Add the current grid location to the used numbers set
        used_numbers.add(r)
        used_numbers.add(c)
    
    # Initialize a variable to store the number of valid assignments
    num_valid_assignments = 0
    
    # Iterate over the valid assignments dictionary
    for location, values in valid_assignments.items():
        # Get the row and column number for the current grid location
        r, c = location
        
        # Initialize a set to store the possible values for the current grid location
        possible_values = set(range(1, n + 1))
        
        # Iterate over the used numbers
        for num in used_numbers:
            # If the current number is not the row or column number, remove it from the possible values
            if num != r and num != c:
                possible_values.remove(num)
        
        # Add the possible values to the valid assignments for the current grid location
        valid_assignments[location] = possible_values
        
        # Increment the number of valid assignments
        num_valid_assignments += len(possible_values)
    
    # Return the number of valid assignments
    return num_valid_assignments

def f2(n, m, t, op):
    # Initialize a dictionary to store the valid assignments for each grid square
    valid_assignments = {}
    
    # Initialize a set to store the used numbers
    used_numbers = set()
    
    # Iterate over the grid locations
    for i in range(m):
        # Read the row and column number for the current grid location
        r, c = map(int, input().split())
        
        # Check if the current grid location is already used
        if (r, c) in valid_assignments:
            # If the current grid location is already used, return 0
            return 0
        
        # Add the current grid location to the valid assignments dictionary
        valid_assignments[(r, c)] = set()
        
        # Add the current grid location to the used numbers set
        used_numbers.add(r)
        used_numbers.add(c)
    
    # Initialize a variable to store the number of valid assignments
    num_valid_assignments = 0
    
    # Iterate over the valid assignments dictionary
    for location, values in valid_assignments.items():
        # Get the row and column number for the current grid location
        r, c = location
        
        # Initialize a set to store the possible values for the current grid location
        possible_values = set(range(1, n + 1))
        
        # Iterate over the used numbers
        for num in used_numbers:
            # If the current number is not the row or column number, remove it from the possible values
            if num != r and num != c:
                possible_values.remove(num)
        
        # Add the possible values to the valid assignments for the current grid location
        valid_assignments[location] = possible_values
        
        # Increment the number of valid assignments
        num_valid_assignments += len(possible_values)
    
    # Return the number of valid assignments
    return num_valid_assignments

if __name__ == '__main__':
    n, m, t, op = map(int, input().split())
    print(f1(n, m, t, op))
    print(f2(n, m, t, op))

