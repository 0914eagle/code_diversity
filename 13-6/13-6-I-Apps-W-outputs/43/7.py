
def get_mappings(maze, instructions):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each possible mapping of digits to directions
    for digit in range(4):
        for direction in ["D", "L", "U", "R"]:
            # Create a copy of the maze and instructions for this mapping
            mapped_maze = maze[:]
            mapped_instructions = instructions[:]
            
            # Map the digit to the direction
            mapped_instructions = mapped_instructions.replace(str(digit), direction)
            
            # Check if the robot can reach the exit with this mapping
            if can_reach_exit(mapped_maze, mapped_instructions):
                # If the robot can reach the exit, add the mapping to the list of mappings
                mappings.append((digit, direction))
    
    # Return the list of mappings
    return mappings

def can_reach_exit(maze, instructions):
    # Initialize the robot's position and direction
    row, col = 0, 0
    direction = "D"
    
    # Loop through each instruction in the string
    for instruction in instructions:
        # Check if the instruction is a digit
        if instruction.isdigit():
            # If the instruction is a digit, map it to a direction based on the current mapping
            direction = mappings[int(instruction)][1]
        else:
            # If the instruction is not a digit, move the robot in the corresponding direction
            if direction == "D":
                row += 1
            elif direction == "L":
                col -= 1
            elif direction == "U":
                row -= 1
            elif direction == "R":
                col += 1
        
        # Check if the robot has reached the exit
        if maze[row][col] == "E":
            return True
    
    # If the robot has not reached the exit, return False
    return False

def main():
    # Read the input maze and instructions
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    instructions = input()
    
    # Get the list of mappings that will lead the robot to the exit
    mappings = get_mappings(maze, instructions)
    
    # Print the number of mappings
    print(len(mappings))

if __name__ == '__main__':
    main()

