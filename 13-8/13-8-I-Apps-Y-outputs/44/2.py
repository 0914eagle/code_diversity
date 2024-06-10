
def get_possible_jumps(n, m, d):
    # Initialize a list to store the possible jumps
    possible_jumps = []
    
    # Iterate over the range of jumps
    for i in range(1, d+1):
        # Check if the current jump is possible
        if i <= m:
            # Add the current jump to the list of possible jumps
            possible_jumps.append(i)
    
    # Return the list of possible jumps
    return possible_jumps

def get_platform_positions(n, m, c):
    # Initialize a list to store the positions of the platforms
    platform_positions = []
    
    # Iterate over the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Iterate over the cells of the current platform
        for j in range(length):
            # Add the current cell to the list of platform positions
            platform_positions.append(i+1)
    
    # Return the list of platform positions
    return platform_positions

def get_jump_sequence(n, m, d, c):
    # Get the possible jumps
    possible_jumps = get_possible_jumps(n, m, d)
    
    # Get the positions of the platforms
    platform_positions = get_platform_positions(n, m, c)
    
    # Initialize a list to store the jump sequence
    jump_sequence = []
    
    # Set the current position to 0
    current_position = 0
    
    # Iterate until the target position is reached
    while current_position < n:
        # Get the possible jumps from the current position
        possible_jumps_from_current = [jump for jump in possible_jumps if current_position + jump <= n]
        
        # Check if there are any possible jumps from the current position
        if len(possible_jumps_from_current) == 0:
            # Return None if there are no possible jumps
            return None
        
        # Get the position of the next platform
        next_platform_position = platform_positions[current_position]
        
        # Get the index of the next platform in the list of possible jumps
        next_platform_index = possible_jumps_from_current.index(next_platform_position - current_position)
        
        # Add the next platform to the jump sequence
        jump_sequence.append(next_platform_index + 1)
        
        # Update the current position
        current_position = next_platform_position
    
    # Return the jump sequence
    return jump_sequence

def main():
    # Read the input
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    # Get the jump sequence
    jump_sequence = get_jump_sequence(n, m, d, c)
    
    # Check if the jump sequence is valid
    if jump_sequence is None:
        # Print NO if the jump sequence is not valid
        print("NO")
    else:
        # Print YES
        print("YES")
        # Print the jump sequence
        print(*jump_sequence)

if __name__ == '__main__':
    main()

