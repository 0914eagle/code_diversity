
def get_mappings(maze):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each digit in the instructions
    for i in range(len(maze)):
        # Check if the current digit is a valid direction
        if maze[i] in ["U", "D", "L", "R"]:
            # If it is, add it to the list of mappings
            mappings.append(maze[i])
    
    # Return the list of mappings
    return mappings

def get_exit_mappings(maze, instructions):
    # Initialize a list to store the mappings that lead to the exit
    exit_mappings = []
    
    # Loop through each mapping of digits to directions
    for mapping in get_mappings(instructions):
        # Initialize a list to store the current position of the robot
        current_position = []
        
        # Loop through each digit in the instructions
        for i in range(len(instructions)):
            # Check if the current digit is a valid direction
            if instructions[i] in ["U", "D", "L", "R"]:
                # If it is, add it to the list of current position
                current_position.append(mapping[instructions[i]])
        
        # Check if the current position is the exit
        if current_position == ["E"]:
            # If it is, add the mapping to the list of mappings that lead to the exit
            exit_mappings.append(mapping)
    
    # Return the list of mappings that lead to the exit
    return exit_mappings

def count_exit_mappings(maze, instructions):
    # Return the number of mappings that lead to the exit
    return len(get_exit_mappings(maze, instructions))

if __name__ == '__main__':
    maze = [
        ["...", "...", "...", "...", "...", "..."],
        [".S.", ".S.", ".S.", ".S.", ".S.", ".S."],
        [".#.", ".#.", ".#.", ".#.", ".#.", ".#."],
        [".#.", ".#.", ".#.", ".#.", ".#.", ".#."],
        ["...", "...", "...", "...", "...", "..."],
        ["...", "...", "...", "...", "...", "..."]
    ]
    instructions = "333300012"
    print(count_exit_mappings(maze, instructions))

