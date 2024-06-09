
def is_reachable(n, m, d, c):
    # Initialize the platform positions
    platforms = [0]
    for i in range(m):
        platforms.append(platforms[i] + c[i])
    platforms.append(n)
    
    # Initialize the jump positions
    jumps = [0]
    
    # Loop through each platform
    for i in range(m):
        # Get the current platform position
        curr_platform = platforms[i]
        
        # Get the next platform position
        next_platform = platforms[i + 1]
        
        # Check if the next platform is within the jump distance
        if next_platform - curr_platform <= d:
            # Add the next platform to the jump positions
            jumps.append(next_platform)
        
        # Check if the current platform is within the jump distance
        if curr_platform - jumps[0] <= d:
            # Remove the current platform from the jump positions
            jumps.remove(curr_platform)
    
    # Check if the last platform is reachable
    if platforms[m] - jumps[0] <= d:
        return True
    else:
        return False

def get_platform_sequence(n, m, d, c):
    # Initialize the platform sequence
    platform_sequence = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Get the current platform position
        curr_platform = platforms[i]
        
        # Get the next platform position
        next_platform = platforms[i + 1]
        
        # Check if the next platform is within the jump distance
        if next_platform - curr_platform <= d:
            # Add the next platform to the platform sequence
            platform_sequence[curr_platform + 1] = i + 1
        
        # Check if the current platform is within the jump distance
        if curr_platform - jumps[0] <= d:
            # Remove the current platform from the platform sequence
            platform_sequence[curr_platform] = 0
    
    return platform_sequence

def main():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    if is_reachable(n, m, d, c):
        print("YES")
        platform_sequence = get_platform_sequence(n, m, d, c)
        print(" ".join(map(str, platform_sequence)))
    else:
        print("NO")

if __name__ == '__main__':
    main()

