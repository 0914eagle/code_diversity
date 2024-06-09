
def solve(grid, commands):
    # Initialize variables
    start, goal = None, None
    obstacles, empty = set(), set()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "S":
                start = (i, j)
            elif char == "G":
                goal = (i, j)
            elif char == "#":
                obstacles.add((i, j))
            else:
                empty.add((i, j))
    
    # Check if the start and goal positions are valid
    if start is None or goal is None:
        return -1
    
    # Initialize the queue with the start position
    queue = [(start, commands)]
    
    # Keep track of the minimum number of changes needed
    min_changes = len(commands)
    
    # Loop through the queue
    while queue:
        position, commands = queue.pop(0)
        
        # If the current position is the goal, return the minimum number of changes needed
        if position == goal:
            return min_changes
        
        # Generate all possible next positions and commands
        for command in ["L", "R", "U", "D"]:
            next_position = (position[0] + (1 if command == "D" else -1) if command in ["D", "U"] else position[0],
                             position[1] + (1 if command == "R" else -1) if command in ["R", "L"] else position[1])
            next_commands = commands[1:]
            
            # If the next position is valid and not an obstacle, add it to the queue
            if next_position in empty and next_position not in obstacles:
                queue.append((next_position, next_commands))
    
    # If the queue is empty, return -1
    return -1

