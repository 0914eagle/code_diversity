
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
        
        # Get the available commands for the current position
        available_commands = get_available_commands(position, obstacles, empty)
        
        # Loop through the available commands
        for command in available_commands:
            # Append the command to the current command string
            new_commands = commands + command
            
            # Get the new position
            new_position = get_new_position(position, command)
            
            # If the new position is valid, add it to the queue
            if new_position in empty:
                queue.append((new_position, new_commands))
    
    # If the queue is empty, return -1
    return -1

def get_available_commands(position, obstacles, empty):
    # Get the available commands for the current position
    available_commands = []
    for command in ["L", "R", "U", "D"]:
        new_position = get_new_position(position, command)
        if new_position in empty and new_position not in obstacles:
            available_commands.append(command)
    
    return available_commands

def get_new_position(position, command):
    # Get the new position based on the command
    if command == "L":
        return position[0], position[1] - 1
    elif command == "R":
        return position[0], position[1] + 1
    elif command == "U":
        return position[0] - 1, position[1]
    else:
        return position[0] + 1, position[1]

grid = [
    "S..",
    ".#.",
    "..G"
]
commands = "DRRDD"
print(solve(grid, commands))

