
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are still available
    available_cells = set(range(1, r + 1))
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the reclaimed cell from the set of available cells
        available_cells.remove(r_i)
        
        # Remove the cells that are not allowed to be reclaimed
        if c_i == 1:
            available_cells.remove(r_i - 1)
            available_cells.remove(r_i + 1)
        else:
            available_cells.remove(r_i - 1)
            available_cells.remove(r_i + 1)
    
    # Check if there are any cells left that can be reclaimed
    if len(available_cells) > 0:
        return "WIN"
    else:
        return "LOSE"

def f2(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are still available
    available_cells = set(range(1, r + 1))
    
    # Iterate through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the reclaimed cell from the set of available cells
        available_cells.remove(r_i)
        
        # Remove the cells that are not allowed to be reclaimed
        if c_i == 1:
            available_cells.remove(r_i - 1)
            available_cells.remove(r_i + 1)
        else:
            available_cells.remove(r_i - 1)
            available_cells.remove(r_i + 1)
    
    # Check if there are any cells left that can be reclaimed
    if len(available_cells) > 0:
        return "LOSE"
    else:
        return "WIN"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

