
def solve(n, m, map):
    # Initialize a 2D array to store the distances from each cell to each state
    distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    
    # Initialize a 2D array to store the previous cell for each cell
    previous = [[-1 for _ in range(n)] for _ in range(m)]
    
    # Initialize a queue to store the cells to be processed
    queue = []
    
    # Initialize the starting cell for each state
    start_cells = [(0, 0), (0, n-1), (m-1, 0), (m-1, n-1)]
    
    # Loop through each starting cell
    for i in range(4):
        # Get the current state and its starting cell
        state = i + 1
        x, y = start_cells[i]
        
        # Set the distance of the starting cell to 0
        distances[x][y] = 0
        
        # Enqueue the starting cell
        queue.append((x, y))
        
        # Loop through the cells in the queue
        while queue:
            # Dequeue a cell
            x, y = queue.pop(0)
            
            # Loop through the four directions
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # Get the next cell
                nx = x + dx
                ny = y + dy
                
                # Check if the next cell is valid
                if 0 <= nx < n and 0 <= ny < m:
                    # Check if the next cell is passable
                    if map[nx][ny] == '.':
                        # Check if the next cell has not been visited
                        if distances[nx][ny] == float('inf'):
                            # Set the distance of the next cell
                            distances[nx][ny] = distances[x][y] + 1
                            
                            # Set the previous cell
                            previous[nx][ny] = (x, y)
                            
                            # Enqueue the next cell
                            queue.append((nx, ny))
    
    # Initialize the minimum number of cells to build a road
    min_cells = float('inf')
    
    # Loop through each state
    for i in range(4):
        # Get the current state
        state = i + 1
        
        # Loop through the cells in the map
        for x in range(n):
            for y in range(m):
                # Check if the current cell belongs to the current state
                if map[x][y] == str(state):
                    # Check if the current cell has been visited
                    if distances[x][y] != float('inf'):
                        # Update the minimum number of cells to build a road
                        min_cells = min(min_cells, distances[x][y])
    
    # Check if the minimum number of cells is infinite
    if min_cells == float('inf'):
        # Return -1 if the goal is unachievable
        return -1
    else:
        # Return the minimum number of cells to build a road
        return min_cells

