
def get_mappings(maze, instructions):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each digit in the instructions
    for i in range(len(instructions)):
        # Get the current digit and the next digit
        current_digit = instructions[i]
        next_digit = instructions[i+1] if i < len(instructions) - 1 else -1
        
        # Check if the current digit is not the same as the next digit
        if current_digit != next_digit:
            # Check if the current digit is 0 or 3 and the next digit is 1 or 2
            if (current_digit == 0 or current_digit == 3) and (next_digit == 1 or next_digit == 2):
                # Add the current digit and the next digit to the mappings list
                mappings.append((current_digit, next_digit))
            # Check if the current digit is 1 or 2 and the next digit is 0 or 3
            elif (current_digit == 1 or current_digit == 2) and (next_digit == 0 or next_digit == 3):
                # Add the current digit and the next digit to the mappings list
                mappings.append((current_digit, next_digit))
    
    # Return the mappings list
    return mappings

def get_exit_mappings(maze, instructions):
    # Get the mappings of digits to directions
    mappings = get_mappings(maze, instructions)
    
    # Initialize a list to store the exit mappings
    exit_mappings = []
    
    # Loop through each mapping
    for mapping in mappings:
        # Get the current digit and the next digit
        current_digit, next_digit = mapping
        
        # Get the current direction and the next direction
        current_direction = get_direction(current_digit)
        next_direction = get_direction(next_digit)
        
        # Check if the current direction and the next direction are valid
        if is_valid_direction(maze, current_direction) and is_valid_direction(maze, next_direction):
            # Add the current mapping to the exit mappings list
            exit_mappings.append(mapping)
    
    # Return the exit mappings list
    return exit_mappings

def get_direction(digit):
    # Check the digit and return the corresponding direction
    if digit == 0:
        return "D"
    elif digit == 1:
        return "L"
    elif digit == 2:
        return "U"
    else:
        return "R"

def is_valid_direction(maze, direction):
    # Check if the direction is valid
    if direction == "D" and maze[1][0] != "#":
        return True
    elif direction == "L" and maze[0][1] != "#":
        return True
    elif direction == "U" and maze[3][0] != "#":
        return True
    else:
        return False

def main():
    # Read the maze and instructions from stdin
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    instructions = input()
    
    # Get the exit mappings
    exit_mappings = get_exit_mappings(maze, instructions)
    
    # Print the number of exit mappings
    print(len(exit_mappings))

if __name__ == '__main__':
    main()

