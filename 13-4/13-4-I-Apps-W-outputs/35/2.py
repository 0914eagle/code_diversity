
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from stdin
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
    
    # Initialize a set to store the cells that can be reclaimed
    available_cells = set(range(1, r + 1))
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the reclaimed cells from the set of available cells
        available_cells.remove(r_i)
    
    # Check if there are any cells that can be reclaimed
    if len(available_cells) == 0:
        # If there are no cells that can be reclaimed, the city loses
        return "LOSE"
    
    # Initialize a variable to store the cell that the city can reclaim
    reclaim_cell = None
    
    # Iterate through the available cells
    for r_i in available_cells:
        # Check if the cell is not allowed to be reclaimed
        if (r_i, 1) in not_allowed_cells or (r_i, 2) in not_allowed_cells:
            # If the cell is not allowed to be reclaimed, continue to the next cell
            continue
        
        # If the cell is allowed to be reclaimed, set it as the cell that the city can reclaim
        reclaim_cell = (r_i, 1)
        break
    
    # Check if the city can reclaim a cell
    if reclaim_cell is None:
        # If the city cannot reclaim a cell, the city loses
        return "LOSE"
    
    # If the city can reclaim a cell, the city wins
    return "WIN"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))

