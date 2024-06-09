
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from stdin
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are not reclaimable
    not_reclaimable_cells = set()
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Add the cells that are not reclaimable to the set
        not_reclaimable_cells.add((r_i - 1, 3 - c_i))
        not_reclaimable_cells.add((r_i, 3 - c_i))
        not_reclaimable_cells.add((r_i + 1, 3 - c_i))
    
    # Initialize a list to store the cells that are reclaimable
    reclaimable_cells = []
    
    # Iterate through the rows
    for r_i in range(1, r + 1):
        # Iterate through the columns
        for c_i in range(1, 3):
            # Check if the cell is not reclaimable
            if (r_i, c_i) not in not_reclaimable_cells:
                # Add the cell to the list of reclaimable cells
                reclaimable_cells.append((r_i, c_i))
    
    # Check if there are any reclaimable cells
    if len(reclaimable_cells) > 0:
        # Return "WIN"
        return "WIN"
    else:
        # Return "LOSE"
        return "LOSE"

def f2(...):
    # TODO: Implement this function
    pass

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))

