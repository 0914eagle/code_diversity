
def can_grasshopper_eat_insect(n, k, line):
    # Initialize the grasshopper's position and the target insect's position
    grasshopper_pos, insect_pos = 0, 0
    
    # Find the position of the grasshopper and the target insect in the line
    for i in range(len(line)):
        if line[i] == "G":
            grasshopper_pos = i
        elif line[i] == "T":
            insect_pos = i
    
    # Initialize a set to keep track of the visited cells
    visited = set()
    
    # Initialize a queue to do the BFS
    queue = [(grasshopper_pos, 0)]
    
    # Loop through the queue
    while queue:
        # Get the current cell and the number of jumps made so far
        cell, jumps = queue.pop(0)
        
        # If the current cell is the target insect's cell, return True
        if cell == insect_pos:
            return True
        
        # If the current cell has already been visited, skip it
        if cell in visited:
            continue
        
        # Mark the current cell as visited
        visited.add(cell)
        
        # Add the neighbors of the current cell to the queue
        for neighbor in [cell + 1, cell - 1]:
            # If the neighbor is within the bounds of the line and is not an obstacle, add it to the queue
            if 0 <= neighbor < n and line[neighbor] != "#":
                queue.append((neighbor, jumps + 1))
    
    # If the queue is empty and the target insect's cell has not been visited, return False
    return False

