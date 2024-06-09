
def get_mappings(maze):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each digit in the instructions
    for i in range(len(maze)):
        # Check if the current digit is a valid direction (0, 1, 2, or 3)
        if maze[i] in [0, 1, 2, 3]:
            # If it is, add the current digit and its corresponding direction to the mappings list
            mappings.append((maze[i], get_direction(maze[i])))
    
    # Return the mappings list
    return mappings

def get_direction(digit):
    # Use a dictionary to map the digits to their corresponding directions
    directions = {0: "D", 1: "L", 2: "U", 3: "R"}
    
    # Return the corresponding direction for the given digit
    return directions[digit]

def find_path(maze, instructions):
    # Initialize a list to store the path
    path = []
    
    # Loop through each instruction in the instructions string
    for i in range(len(instructions)):
        # Get the current instruction and its corresponding direction
        instruction = instructions[i]
        direction = get_direction(instruction)
        
        # Check if the current direction is valid (i.e., not off the edge of the maze or hit an obstacle)
        if is_valid_direction(maze, direction):
            # If it is, add the current direction to the path list
            path.append(direction)
        else:
            # If it's not, break out of the loop and return False
            break
    
    # If we reach the end of the instructions string, return True
    if i == len(instructions) - 1:
        return True
    else:
        return False

def is_valid_direction(maze, direction):
    # Get the current position of the robot
    row, col = get_position(maze)
    
    # Check if the current direction is valid based on the maze layout
    if direction == "D" and row + 1 < len(maze) and maze[row + 1][col] != '#':
        return True
    elif direction == "L" and col - 1 >= 0 and maze[row][col - 1] != '#':
        return True
    elif direction == "U" and row - 1 >= 0 and maze[row - 1][col] != '#':
        return True
    elif direction == "R" and col + 1 < len(maze[0]) and maze[row][col + 1] != '#':
        return True
    else:
        return False

def get_position(maze):
    # Initialize variables to store the position of the robot
    row, col = 0, 0
    
    # Loop through each row in the maze
    for i in range(len(maze)):
        # Loop through each column in the current row
        for j in range(len(maze[i])):
            # If the current position is the start position, return its row and column indices
            if maze[i][j] == 'S':
                row, col = i, j
                break
    
    # Return the row and column indices of the start position
    return row, col

def count_mappings(maze, instructions):
    # Initialize a variable to store the number of valid mappings
    count = 0
    
    # Loop through each possible mapping of digits to directions
    for mapping in get_mappings(instructions):
        # Check if the current mapping leads to the exit
        if find_path(maze, mapping):
            # If it does, increment the count
            count += 1
    
    # Return the count of valid mappings
    return count

def main():
    # Read the input maze and instructions
    maze = [input().strip() for _ in range(int(input()))]
    instructions = input().strip()
    
    # Print the number of mappings of digits to directions that lead to the exit
    print(count_mappings(maze, instructions))

if __name__ == '__main__':
    main()

