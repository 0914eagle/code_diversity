
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Loop through the reclaimed cells
    for i in range(n):
        # Read the next reclaimed cell
        r_i, c_i = map(int, input().split())
        
        # Add the reclaimed cell to the list
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the available cells
    available_cells = set([(i, j) for i in range(1, r + 1) for j in range(1, 3)])
    
    # Loop through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the reclaimed cell from the available cells
        available_cells.remove((r_i, c_i))
        
        # Remove the cells that are not allowed to be reclaimed
        available_cells.remove((r_i - 1, 3 - c_i))
        available_cells.remove((r_i, 3 - c_i))
        available_cells.remove((r_i + 1, 3 - c_i))
    
    # Check if there are any available cells left
    if len(available_cells) > 0:
        return "WIN"
    else:
        return "LOSE"

def f2(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Loop through the reclaimed cells
    for i in range(n):
        # Read the next reclaimed cell
        r_i, c_i = map(int, input().split())
        
        # Add the reclaimed cell to the list
        reclaimed_cells.append((r_i, c_i))
    
    # Initialize a set to store the available cells
    available_cells = set([(i, j) for i in range(1, r + 1) for j in range(1, 3)])
    
    # Loop through the reclaimed cells
    for r_i, c_i in reclaimed_cells:
        # Remove the reclaimed cell from the available cells
        available_cells.remove((r_i, c_i))
        
        # Remove the cells that are not allowed to be reclaimed
        available_cells.remove((r_i - 1, 3 - c_i))
        available_cells.remove((r_i, 3 - c_i))
        available_cells.remove((r_i + 1, 3 - c_i))
    
    # Check if there are any available cells left
    if len(available_cells) > 0:
        return "WIN"
    else:
        return "LOSE"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

