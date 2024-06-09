
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are not allowed to be reclaimed
    not_allowed_cells = set()
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Add the cells that are not allowed to be reclaimed to the set
        not_allowed_cells.add((r_i - 1, 3 - c_i))
        not_allowed_cells.add((r_i, 3 - c_i))
        not_allowed_cells.add((r_i + 1, 3 - c_i))
    
    # Initialize a list to store the cells that are available for reclaiming
    available_cells = []
    
    # Iterate through the rows
    for r_i in range(1, r + 1):
        # Iterate through the columns
        for c_i in range(1, 3):
            # Check if the cell is not allowed to be reclaimed
            if (r_i, c_i) not in not_allowed_cells:
                # Add the cell to the list of available cells
                available_cells.append((r_i, c_i))
    
    # Check if there are any available cells
    if len(available_cells) == 0:
        # Return "LOSE" if there are no available cells
        return "LOSE"
    else:
        # Return "WIN" if there are available cells
        return "WIN"

def f2(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are not allowed to be reclaimed
    not_allowed_cells = set()
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Add the cells that are not allowed to be reclaimed to the set
        not_allowed_cells.add((r_i - 1, 3 - c_i))
        not_allowed_cells.add((r_i, 3 - c_i))
        not_allowed_cells.add((r_i + 1, 3 - c_i))
    
    # Initialize a list to store the cells that are available for reclaiming
    available_cells = []
    
    # Iterate through the rows
    for r_i in range(1, r + 1):
        # Iterate through the columns
        for c_i in range(1, 3):
            # Check if the cell is not allowed to be reclaimed
            if (r_i, c_i) not in not_allowed_cells:
                # Add the cell to the list of available cells
                available_cells.append((r_i, c_i))
    
    # Check if there are any available cells
    if len(available_cells) == 0:
        # Return "LOSE" if there are no available cells
        return "LOSE"
    else:
        # Return "WIN" if there are available cells
        return "WIN"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

