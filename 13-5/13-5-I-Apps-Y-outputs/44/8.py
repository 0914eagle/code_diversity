
def is_possible(n, m, d, c):
    # Initialize variables
    platforms = [[0] * (c[i] + 1) for i in range(m)]
    jump_positions = []
    current_position = 0
    
    # Move platforms until we start jumping
    while current_position < n:
        # Find the next platform to move
        next_platform = -1
        for i in range(m):
            if platforms[i][current_position] == 1:
                next_platform = i
                break
        
        # Move the platform to the left or right
        if next_platform != -1:
            platforms[next_platform] = [0] + platforms[next_platform][1:]
            current_position += 1
        else:
            break
    
    # Start jumping
    while current_position < n:
        # Find the next platform to jump to
        next_platform = -1
        for i in range(m):
            if platforms[i][current_position + d] == 1:
                next_platform = i
                break
        
        # Jump to the next platform
        if next_platform != -1:
            platforms[next_platform] = [0] + platforms[next_platform][1:]
            current_position += d
            jump_positions.append(current_position)
        else:
            break
    
    # Check if we reached the end of the river
    if current_position == n:
        return True, jump_positions
    else:
        return False, []

def get_platform_sequence(n, m, d, c, jump_positions):
    platforms = [[0] * (c[i] + 1) for i in range(m)]
    platform_sequence = [0] * n
    
    for i in range(m):
        for j in range(c[i]):
            if j + 1 in jump_positions:
                platform_sequence[j + 1] = i + 1
    
    return platform_sequence

def main():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    possible, jump_positions = is_possible(n, m, d, c)
    if possible:
        platform_sequence = get_platform_sequence(n, m, d, c, jump_positions)
        print("YES")
        print(" ".join(map(str, platform_sequence)))
    else:
        print("NO")

if __name__ == '__main__':
    main()

