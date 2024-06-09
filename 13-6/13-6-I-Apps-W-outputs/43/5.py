
def get_mappings(maze, instructions):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each possible mapping of digits to directions
    for d0 in range(4):
        for d1 in range(4):
            for d2 in range(4):
                for d3 in range(4):
                    # Check if the current mapping is valid
                    if is_valid_mapping(maze, instructions, d0, d1, d2, d3):
                        # If valid, add it to the list of mappings
                        mappings.append((d0, d1, d2, d3))
    
    return mappings

def is_valid_mapping(maze, instructions, d0, d1, d2, d3):
    # Initialize the robot's position and direction
    row, col = 0, 0
    direction = "R"
    
    # Loop through each instruction in the string
    for i in range(len(instructions)):
        # Get the current instruction
        instruction = instructions[i]
        
        # Check if the current instruction is a valid digit
        if instruction not in "0123":
            return False
        
        # Get the current direction based on the mapping
        if instruction == "0":
            direction = "R"
        elif instruction == "1":
            direction = "L"
        elif instruction == "2":
            direction = "U"
        elif instruction == "3":
            direction = "D"
        
        # Move the robot in the current direction
        if direction == "R":
            col += 1
        elif direction == "L":
            col -= 1
        elif direction == "U":
            row -= 1
        elif direction == "D":
            row += 1
        
        # Check if the robot has reached the edge of the maze or hit an obstacle
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == "#":
            return False
    
    # Check if the robot has reached the exit
    if maze[row][col] == "E":
        return True
    else:
        return False

def count_mappings(maze, instructions):
    # Get the list of valid mappings
    mappings = get_mappings(maze, instructions)
    
    # Return the number of valid mappings
    return len(mappings)

if __name__ == '__main__':
    while True:
        # Read the input
        n, m = map(int, input().split())
        maze = [input() for _ in range(n)]
        instructions = input()
        
        # Solve the problem
        count = count_mappings(maze, instructions)
        
        # Print the output
        print(count)

