
def solve(N, R, C, petals):
    # Initialize a list to store the number of petals on each flower
    num_petals = [[0] * N for _ in range(N)]
    for i in range(N):
        for j, petal in enumerate(petals[i]):
            num_petals[i][j] = petal
    
    # Initialize a set to store the visited flowers
    visited = set()
    
    # Initialize a variable to store the maximum number of flowers visited
    max_visited = 0
    
    # Initialize a queue to store the next positions to visit
    queue = [(R, C)]
    
    # Loop through the queue
    while queue:
        # Get the current position
        r, c = queue.pop(0)
        
        # If the current position is not visited, mark it as visited and increase the number of visited flowers
        if (r, c) not in visited:
            visited.add((r, c))
            max_visited += 1
            
            # Get the number of petals on the current flower
            num_petals_current = num_petals[r - 1][c - 1]
            
            # Get the adjacent positions
            adjacent = []
            if r > 1:
                adjacent.append((r - 1, c))
            if r < N:
                adjacent.append((r + 1, c))
            if c > 1:
                adjacent.append((r, c - 1))
            if c < N:
                adjacent.append((r, c + 1))
            
            # Add the adjacent positions to the queue if they are not visited and the number of petals is larger than the current flower
            for r_, c_ in adjacent:
                if (r_, c_) not in visited and num_petals[r_ - 1][c_ - 1] > num_petals_current:
                    queue.append((r_, c_))
    
    return max_visited

