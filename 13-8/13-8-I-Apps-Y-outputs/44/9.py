
def get_platform_sequence(n, m, d, c):
    # Initialize the platform sequence as a list of 0s
    platform_sequence = [0] * (n + 2)
    
    # Iterate over the platforms
    for i in range(m):
        # Get the length of the current platform
        platform_length = c[i]
        
        # Iterate over the cells of the current platform
        for j in range(platform_length):
            # Get the cell number
            cell_number = j + 1
            
            # Set the platform index in the platform sequence
            platform_sequence[cell_number] = i + 1
    
    return platform_sequence

def can_reach_n_from_0(n, m, d, c):
    # Get the platform sequence
    platform_sequence = get_platform_sequence(n, m, d, c)
    
    # Initialize the position as 0
    position = 0
    
    # Initialize the jumps as 0
    jumps = 0
    
    # Iterate until the position is n + 1
    while position < n + 1:
        # Get the platform index of the current position
        platform_index = platform_sequence[position]
        
        # Check if the platform index is 0 (meaning the position is not on a platform)
        if platform_index == 0:
            # Return False if the position is not on a platform and we cannot jump
            if jumps == 0:
                return False
            else:
                # Decrement the jumps
                jumps -= 1
        else:
            # Increment the position
            position += 1
            # Increment the jumps
            jumps += 1
    
    # Return True if we reached n + 1
    return True

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print("YES" if can_reach_n_from_0(n, m, d, c) else "NO")

