
def valid_colorings(n, a):
    # Initialize the number of valid colorings to 0
    num_valid_colorings = 0
    
    # Loop through all possible colorings
    for coloring in itertools.product(range(7), repeat=n):
        # Check if the coloring is valid
        if is_valid_coloring(n, a, coloring):
            # Increment the number of valid colorings
            num_valid_colorings += 1
    
    # Return the number of valid colorings
    return num_valid_colorings

def is_valid_coloring(n, a, coloring):
    # Initialize the number of colored edges to 0
    num_colored_edges = 0
    
    # Loop through all hexagons
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Check if the current hexagon is colored
            if coloring[i-1] != -1:
                # Increment the number of colored edges
                num_colored_edges += 1
            
            # Check if the current hexagon is adjacent to a colored hexagon
            if a[i-1][j-1] != -1 and coloring[i-1] == coloring[a[i-1][j-1]-1]:
                # Return False if the current hexagon is adjacent to a colored hexagon with the same color
                return False
    
    # Return True if the number of colored edges is equal to the number of edges in the grid
    return num_colored_edges == n * (n-1)

