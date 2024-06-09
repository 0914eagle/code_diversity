
import itertools

def get_mappings(directions, instructions):
    # Initialize a list to store the mappings
    mappings = []
    
    # Iterate over the possible mappings of directions to instructions
    for mapping in itertools.product(directions, repeat=len(instructions)):
        # Check if the current mapping leads to the exit
        if is_valid_mapping(mapping, instructions):
            # If it does, add it to the list of mappings
            mappings.append(mapping)
    
    return mappings

def is_valid_mapping(mapping, instructions):
    # Initialize the robot's position and direction
    position = (0, 0)
    direction = (0, 1)
    
    # Iterate over the instructions
    for instruction in instructions:
        # Get the new direction based on the current direction and the current instruction
        new_direction = get_new_direction(direction, mapping[instruction])
        
        # Check if the new position is valid
        if is_valid_position(position[0] + new_direction[0], position[1] + new_direction[1]):
            # If it is, update the position and direction
            position = (position[0] + new_direction[0], position[1] + new_direction[1])
            direction = new_direction
        else:
            # If it's not, return False
            return False
    
    # If the robot reaches the exit, return True
    if position == (4, 4):
        return True
    else:
        return False

def get_new_direction(current_direction, instruction):
    # Initialize a dictionary to map instructions to directions
    directions = {
        "0": (0, 1),
        "1": (-1, 0),
        "2": (0, -1),
        "3": (1, 0)
    }
    
    # Return the new direction based on the current direction and the instruction
    return directions[instruction]

def is_valid_position(x, y):
    # Check if the position is within the bounds of the maze
    if x >= 0 and x < 5 and y >= 0 and y < 5:
        # If it is, check if it's not an obstacle
        if maze[x][y] != "#":
            # If it's not, return True
            return True
    
    # If the position is not valid, return False
    return False

def main():
    # Read the input
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    instructions = input()
    
    # Get the mappings of directions to instructions
    mappings = get_mappings(["0", "1", "2", "3"], instructions)
    
    # Print the number of valid mappings
    print(len(mappings))

if __name__ == '__main__':
    main()

