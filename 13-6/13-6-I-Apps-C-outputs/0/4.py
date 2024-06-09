
def read_input():
    n, m, t, op = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    return n, m, t, op, grid

def get_valid_assignments(n, m, t, op, grid):
    # Initialize a set to store the valid assignments
    valid_assignments = set()
    
    # Iterate over each grid square in the section
    for i in range(m):
        for j in range(m):
            # Get the value of the current grid square
            value = grid[i][j]
            
            # If the value is not already in the valid assignments set, add it
            if value not in valid_assignments:
                valid_assignments.add(value)
            
            # If the value is the target value, add it to the valid assignments set
            if value == t:
                valid_assignments.add(value)
    
    # Return the number of valid assignments
    return len(valid_assignments)

def main():
    n, m, t, op, grid = read_input()
    print(get_valid_assignments(n, m, t, op, grid))

if __name__ == '__main__':
    main()

