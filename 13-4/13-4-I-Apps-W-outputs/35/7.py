
def f1(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the input cells
    for i in range(n):
        # Read the current cell
        r_i, c_i = map(int, input().split())
        
        # Check if the current cell has already been reclaimed
        if (r_i, c_i) in reclaimed_cells:
            continue
        
        # Reclaim the current cell
        reclaimed_cells.append((r_i, c_i))
    
    # Check if the last cell can be reclaimed
    if len(reclaimed_cells) == r:
        return "WIN"
    else:
        return "LOSE"

def f2(r, n):
    # Initialize a list to store the reclaimed cells
    reclaimed_cells = []
    
    # Iterate through the input cells
    for i in range(n):
        # Read the current cell
        r_i, c_i = map(int, input().split())
        
        # Check if the current cell has already been reclaimed
        if (r_i, c_i) in reclaimed_cells:
            continue
        
        # Reclaim the current cell
        reclaimed_cells.append((r_i, c_i))
    
    # Check if the last cell can be reclaimed
    if len(reclaimed_cells) == r:
        return "WIN"
    else:
        return "LOSE"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

