
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Loop through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are still available
    available_cells = set(range(1, r + 1))
    
    # Loop through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the cell from the set of available cells
        available_cells.remove(r_i)
        available_cells.remove(c_i)
    
    # Check if there are any cells left that can be reclaimed
    if len(available_cells) > 0:
        return "WIN"
    else:
        return "LOSE"

def f2(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Loop through the reclaimed cells
    for i in range(n):
        # Read the next cell from the input
        r_i, c_i = map(int, input().split())
        
        # Add the cell to the list of reclaimed cells
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the cells that are still available
    available_cells = set(range(1, r + 1))
    
    # Loop through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the cell from the set of available cells
        available_cells.remove(r_i)
        available_cells.remove(c_i)
    
    # Check if there are any cells left that can be reclaimed
    if len(available_cells) > 0:
        return "WIN"
    else:
        return "LOSE"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

