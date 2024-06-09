
def f1(n, m, p):
    # Initialize the number of ways to place the minimum number of obstacles
    num_ways = 0
    
    # Loop through all possible positions for the top-left corner of the block
    for i in range(n):
        for j in range(m):
            # Check if the current position is valid
            if valid_position(i, j, n, m):
                # Increment the number of ways to place the minimum number of obstacles
                num_ways += 1
    
    # Return the number of ways modulo p
    return num_ways % p

def valid_position(i, j, n, m):
    # Check if the current position is within the bounds of the grid
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    
    # Check if the current position is axis-aligned with the block
    if i % 2 == 0 and j % 2 == 0:
        return False
    
    # Check if the current position is in a subgrid that contains at least one obstacle
    for k in range(i, i + 2):
        for l in range(j, j + 2):
            if k < 0 or k >= n or l < 0 or l >= m:
                return False
    
    return True

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    print(f1(n, m, p))

