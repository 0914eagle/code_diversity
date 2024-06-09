
import itertools

def get_mappings(n, m, s):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through all possible mappings of digits to directions
    for mapping in itertools.permutations([0, 1, 2, 3], n):
        # Check if the mapping is valid
        if is_valid_mapping(n, m, s, mapping):
            # If the mapping is valid, add it to the list of mappings
            mappings.append(mapping)
    
    # Return the list of mappings
    return mappings

def is_valid_mapping(n, m, s, mapping):
    # Initialize a list to store the robot's position
    position = [0, 0]
    
    # Loop through the instructions in the string
    for i in range(n):
        # Get the current instruction
        instruction = s[i]
        
        # Check if the instruction is valid
        if instruction not in mapping:
            # If the instruction is not valid, return False
            return False
        
        # Get the direction corresponding to the instruction
        direction = mapping[instruction]
        
        # Move the robot in the direction corresponding to the instruction
        if direction == "U":
            position[0] -= 1
        elif direction == "D":
            position[0] += 1
        elif direction == "L":
            position[1] -= 1
        elif direction == "R":
            position[1] += 1
        
        # Check if the robot has reached the exit
        if position == [m - 1, n - 1]:
            # If the robot has reached the exit, return True
            return True
        
        # Check if the robot has hit an obstacle
        if maze[position[0]][position[1]] == "#":
            # If the robot has hit an obstacle, return False
            return False
    
    # If the robot has not reached the exit and has not hit an obstacle, return True
    return True

def main():
    # Read the input
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    s = input()
    
    # Get the mappings of digits to directions
    mappings = get_mappings(n, m, s)
    
    # Print the number of mappings
    print(len(mappings))

if __name__ == '__main__':
    main()

