
def find_path(x0, y0, x1, y1, segments):
    # Initialize a set to store the allowed cells
    allowed_cells = set()
    
    # Loop through the segments and add the allowed cells to the set
    for r, a, b in segments:
        for c in range(a, b + 1):
            allowed_cells.add((r, c))
    
    # Check if the initial position is an allowed cell
    if (x0, y0) not in allowed_cells:
        return -1
    
    # Initialize a queue to store the cells to be visited
    queue = [(x0, y0, 0)]
    
    # Loop until the queue is empty
    while queue:
        # Get the current cell and its distance from the initial position
        cell, distance = queue.pop(0)
        
        # Check if the current cell is the final position
        if cell == (x1, y1):
            return distance
        
        # Get the neighbors of the current cell
        neighbors = [(cell[0], cell[1] + 1), (cell[0], cell[1] - 1), (cell[0] + 1, cell[1]), (cell[0] - 1, cell[1])]
        
        # Loop through the neighbors and add them to the queue if they are allowed cells
        for neighbor in neighbors:
            if neighbor in allowed_cells:
                queue.append((neighbor[0], neighbor[1], distance + 1))
    
    # If the queue is empty, there is no path between the initial and final positions
    return -1

