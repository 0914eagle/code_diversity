
def find_path(x0, y0, x1, y1, segments):
    # Initialize a set to store the allowed cells
    allowed_cells = set()
    
    # Loop through the segments and add the allowed cells to the set
    for r, a, b in segments:
        for c in range(a, b + 1):
            allowed_cells.add((r, c))
    
    # Check if the initial position is allowed
    if (x0, y0) not in allowed_cells:
        return -1
    
    # Initialize a queue to store the cells to be visited
    queue = [(x0, y0, 0)]
    
    # Loop until the queue is empty
    while queue:
        # Get the current cell and its distance from the initial position
        x, y, dist = queue.pop(0)
        
        # If the current cell is the final position, return the distance
        if x == x1 and y == y1:
            return dist
        
        # Loop through the neighboring cells
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Get the neighboring cell
            nx = x + dx
            ny = y + dy
            
            # Check if the neighboring cell is allowed and not visited before
            if (nx, ny) in allowed_cells and (nx, ny) not in queue:
                # Add the neighboring cell to the queue and increment its distance
                queue.append((nx, ny, dist + 1))
    
    # If the final position is not reached, return -1
    return -1

