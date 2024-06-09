
def kenkent(n, m, t, op):
    # Initialize a dictionary to store the valid assignments for each grid square
    assignments = {}
    
    # Iterate through each grid square
    for r in range(1, n+1):
        for c in range(1, n+1):
            # If the grid square is in the section, add it to the dictionary with a value of None
            if (r, c) in grid:
                assignments[(r, c)] = None
    
    # Initialize a list to store the valid assignments for the section
    valid_assignments = []
    
    # Function to recursively search for valid assignments
    def search(assignment):
        # If all grid squares in the section have been assigned, add the assignment to the list of valid assignments
        if len(assignment) == m:
            valid_assignments.append(assignment)
            return
        
        # Get the next grid square to assign
        next_square = None
        for square in assignment:
            if assignment[square] is None:
                next_square = square
                break
        
        # If no grid square can be assigned, return
        if next_square is None:
            return
        
        # Get the row and column of the next grid square
        r, c = next_square
        
        # Get the values of the grid squares in the same row and column as the next grid square
        row_values = [assignments[(r, c_)] for c_ in range(1, n+1) if (r, c_) in assignments]
        col_values = [assignments[(r_, c)] for r_ in range(1, n+1) if (r_, c) in assignments]
        
        # Get the available values for the next grid square based on the arithmetic operator
        if op == '+':
            available_values = [v for v in range(1, n+1) if v not in row_values and v not in col_values]
        elif op == '-':
            available_values = [v for v in range(1, n+1) if v not in row_values and v not in col_values and v != 0]
        elif op == '*':
            available_values = [v for v in range(1, n+1) if v not in row_values and v not in col_values and v != 0 and v != 1]
        elif op == '/':
            available_values = [v for v in range(1, n+1) if v not in row_values and v not in col_values and v != 0 and v != 1 and v != n]
        
        # Recursively search for valid assignments for each available value
        for v in available_values:
            assignment[next_square] = v
            search(assignment)
            assignment[next_square] = None
    
    # Search for valid assignments
    search({})
    
    # Return the number of valid assignments
    return len(valid_assignments)

def main():
    # Read input
    n, m, t, op = map(int, input().split())
    grid = set()
    for _ in range(m):
        r, c = map(int, input().split())
        grid.add((r, c))
    
    # Solve the problem
    result = kenkent(n, m, t, op)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

