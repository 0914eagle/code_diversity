
def get_platform_placement(n, m, c, d):
    # Initialize variables
    platforms = [0] * (n + 2)
    for i in range(m):
        platforms[c[i] - 1] = i + 1
    return platforms

def can_reach_end(n, m, c, d):
    # Get the platform placement
    platforms = get_platform_placement(n, m, c, d)
    
    # Initialize variables
    current_position = 0
    jump_positions = []
    
    # Loop through the platforms
    for i in range(m):
        # Get the current platform
        platform = platforms[c[i] - 1]
        
        # Check if the platform is in range
        if platform == 0 or platform == m + 1:
            continue
        
        # Get the jump positions for the current platform
        jump_positions.extend(range(current_position + 1, current_position + d + 1))
        
        # Update the current position
        current_position = current_position + d
    
    # Check if the final position is reachable
    if current_position == n:
        return True
    else:
        return False

def get_platform_sequence(n, m, c, d):
    # Get the platform placement
    platforms = get_platform_placement(n, m, c, d)
    
    # Initialize variables
    platform_sequence = [0] * (n + 2)
    
    # Loop through the platforms
    for i in range(m):
        # Get the current platform
        platform = platforms[c[i] - 1]
        
        # Check if the platform is in range
        if platform == 0 or platform == m + 1:
            continue
        
        # Update the platform sequence
        platform_sequence[c[i] - 1] = platform
    
    return platform_sequence

def main():
    # Read the input
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    # Check if the final position is reachable
    if can_reach_end(n, m, c, d):
        print("YES")
        platform_sequence = get_platform_sequence(n, m, c, d)
        print(*platform_sequence)
    else:
        print("NO")

if __name__ == '__main__':
    main()

