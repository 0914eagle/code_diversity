
import itertools

def get_mappings(s):
    # Get all possible mappings of digits to directions
    mappings = []
    for mapping in itertools.product([0, 1, 2, 3], repeat=4):
        mappings.append(mapping)
    
    # Filter out mappings that don't lead to the exit
    valid_mappings = []
    for mapping in mappings:
        if is_valid_mapping(s, mapping):
            valid_mappings.append(mapping)
    
    return valid_mappings

def is_valid_mapping(s, mapping):
    # Initialize the robot's position and direction
    position = (0, 0)
    direction = 0
    
    # Iterate through the instructions and update the robot's position and direction
    for i in range(len(s)):
        instruction = s[i]
        direction = mapping[instruction]
        if direction == 0:
            position = (position[0] + 1, position[1])
        elif direction == 1:
            position = (position[0], position[1] - 1)
        elif direction == 2:
            position = (position[0] - 1, position[1])
        elif direction == 3:
            position = (position[0], position[1] + 1)
    
    # Check if the robot reached the exit
    if position == (4, 4):
        return True
    else:
        return False

def count_mappings(s):
    # Get all valid mappings of digits to directions
    mappings = get_mappings(s)
    
    # Count the number of valid mappings
    count = len(mappings)
    
    return count

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    s = input()
    count = count_mappings(s)
    print(count)

