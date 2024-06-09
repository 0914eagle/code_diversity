
def is_reachable(n, m, d, c):
    # Initialize the platform positions and the current position
    platforms = [0]
    current_position = 0
    
    # Iterate through the platforms
    for i in range(m):
        # Check if the current platform overlaps with the previous platform
        if current_position + c[i] > platforms[-1]:
            # If it does, return False
            return False
        
        # Add the current platform to the list of platforms
        platforms.append(current_position + c[i])
        
        # Update the current position
        current_position = platforms[-1]
    
    # Check if the last platform overlaps with the first platform
    if current_position + d > platforms[0]:
        # If it does, return False
        return False
    
    # If all platforms are valid, return True
    return True

def move_platforms(n, m, d, c):
    # Initialize the platform positions and the current position
    platforms = [0]
    current_position = 0
    
    # Iterate through the platforms
    for i in range(m):
        # Check if the current platform overlaps with the previous platform
        if current_position + c[i] > platforms[-1]:
            # If it does, move the current platform to the left
            platforms[-1] = current_position + c[i]
        
        # Add the current platform to the list of platforms
        platforms.append(current_position + c[i])
        
        # Update the current position
        current_position = platforms[-1]
    
    # Check if the last platform overlaps with the first platform
    if current_position + d > platforms[0]:
        # If it does, move the last platform to the right
        platforms[0] = current_position + d
    
    # Return the updated platform positions
    return platforms

def get_jump_sequence(n, m, d, c):
    # Initialize the jump sequence
    jump_sequence = []
    
    # Iterate through the platforms
    for i in range(m):
        # Add the current platform to the jump sequence
        jump_sequence.append(platforms[i])
        
        # Update the current position
        current_position = platforms[i] + c[i]
    
    # Add the last platform to the jump sequence
    jump_sequence.append(platforms[-1] + d)
    
    # Return the jump sequence
    return jump_sequence

def get_platform_sequence(n, m, d, c):
    # Initialize the platform sequence
    platform_sequence = [0] * (n + 2)
    
    # Iterate through the platforms
    for i in range(m):
        # Add the current platform to the platform sequence
        platform_sequence[platforms[i]] = i + 1
        
        # Update the current position
        current_position = platforms[i] + c[i]
    
    # Add the last platform to the platform sequence
    platform_sequence[platforms[-1] + d] = m + 1
    
    # Return the platform sequence
    return platform_sequence

def main():
    # Read the input
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    # Check if it is possible to reach the end of the river
    if is_reachable(n, m, d, c):
        # Move the platforms to the left or right as needed
        platforms = move_platforms(n, m, d, c)
        
        # Get the jump sequence
        jump_sequence = get_jump_sequence(n, m, d, c)
        
        # Get the platform sequence
        platform_sequence = get_platform_sequence(n, m, d, c)
        
        # Print the answer
        print("YES")
        print(" ".join(map(str, platform_sequence)))
    else:
        # Print the answer
        print("NO")

if __name__ == '__main__':
    main()

