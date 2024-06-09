
def count_valid_colorings(n, a):
    # Initialize the number of valid colorings to 0
    num_valid_colorings = 0
    
    # Loop through each row of the grid
    for i in range(1, n+1):
        # If the row is odd, there are n hexagons in the row
        if i % 2 == 1:
            num_hexagons = n
        # If the row is even, there are n-1 hexagons in the row
        else:
            num_hexagons = n-1
        
        # Loop through each hexagon in the row
        for j in range(1, num_hexagons+1):
            # If the current hexagon is not colored, skip it
            if a[i-1][j-1] == -1:
                continue
            
            # If the current hexagon is colored, check if it forms a loop
            else:
                # Initialize the number of colored edges to 0
                num_colored_edges = 0
                
                # Loop through the neighbors of the current hexagon
                for neighbor in get_neighbors(i, j, n):
                    # If the neighbor is not colored, skip it
                    if a[neighbor[0]-1][neighbor[1]-1] == -1:
                        continue
                    
                    # If the neighbor is colored, check if it forms a loop with the current hexagon
                    else:
                        # If the neighbor is colored with the same color as the current hexagon, increment the number of colored edges
                        if a[neighbor[0]-1][neighbor[1]-1] == a[i-1][j-1]:
                            num_colored_edges += 1
                
                # If the number of colored edges is equal to the number of neighbors, the current hexagon forms a loop
                if num_colored_edges == num_hexagons:
                    num_valid_colorings += 1
    
    # Return the number of valid colorings
    return num_valid_colorings

# Function to get the neighbors of a hexagon
def get_neighbors(i, j, n):
    # Initialize the list of neighbors
    neighbors = []
    
    # If the hexagon is in the first row, it has three neighbors
    if i == 1:
        neighbors = [(i, j-1), (i, j+1), (i+1, j)]
    
    # If the hexagon is in the last row, it has three neighbors
    elif i == n:
        neighbors = [(i, j-1), (i, j+1), (i-1, j)]
    
    # If the hexagon is in the middle rows, it has six neighbors
    else:
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    
    # Return the list of neighbors
    return neighbors

