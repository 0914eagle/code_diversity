
def solve(n, m, map):
    # Initialize a dictionary to store the number of cells needed to reach each state
    states = {1: 0, 2: 0, 3: 0}
    
    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable, update the number of cells needed to reach each state
            if map[i][j] != '#':
                states[map[i][j]] += 1
    
    # Initialize a variable to store the minimum number of cells needed to build a road
    min_cells = float('inf')
    
    # Loop through each state and calculate the minimum number of cells needed to build a road to connect all cells of that state
    for state in states:
        min_cells = min(min_cells, states[state])
    
    # Return the minimum number of cells needed to build a road
    return min_cells

