
import itertools

def get_mappings(n, m, maze, instructions):
    # Initialize a list to store the mappings
    mappings = []
    
    # Iterate over all possible mappings of digits to directions
    for mapping in itertools.product(range(4), repeat=n):
        # Check if the current mapping leads to the exit
        if check_mapping(n, m, maze, instructions, mapping):
            # If it does, add it to the list of mappings
            mappings.append(mapping)
    
    # Return the list of mappings
    return mappings

def check_mapping(n, m, maze, instructions, mapping):
    # Initialize the robot's position and direction
    x, y = 0, 0
    direction = 0
    
    # Iterate over the instructions
    for instruction in instructions:
        # Get the current direction based on the mapping
        direction = mapping[int(instruction)]
        
        # Update the robot's position based on the direction
        if direction == 0:
            y += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x += 1
        
        # Check if the robot has reached the exit
        if maze[y][x] == 'E':
            return True
        
        # Check if the robot has hit an obstacle or gone off the edge of the maze
        if x < 0 or x >= m or y < 0 or y >= n or maze[y][x] == '#':
            return False
    
    # If the robot has not reached the exit, return False
    return False

def main():
    # Read the input
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    instructions = input()
    
    # Get the mappings that lead to the exit
    mappings = get_mappings(n, m, maze, instructions)
    
    # Print the number of mappings
    print(len(mappings))

if __name__ == '__main__':
    main()

