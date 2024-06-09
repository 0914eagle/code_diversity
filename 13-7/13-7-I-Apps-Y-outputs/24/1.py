
def solve(M, N, vault):
    # Initialize a 2D array to store the shortest distance from the starting point to each position in the vault
    dist = [[float("inf") for _ in range(N)] for _ in range(M)]
    # Initialize a 2D array to store the previous position of the shortest path from the starting point to each position in the vault
    prev = [[-1 for _ in range(N)] for _ in range(M)]
    
    # Set the starting point as the north west corner with distance 0
    dist[0][0] = 0
    prev[0][0] = -1
    
    # Loop through each position in the vault
    for i in range(M):
        for j in range(N):
            # If the current position is not the starting point, check if the previous position is not -1
            if prev[i][j] != -1:
                # Get the previous position
                pi = prev[i][j] // N
                pj = prev[i][j] % N
                # Check if the previous position is not the starting point
                if pi != 0 or pj != 0:
                    # Get the distance from the previous position to the current position
                    d = vault[pi][pj]
                    # If the distance is less than the current shortest distance, update the shortest distance and previous position
                    if dist[i][j] > dist[pi][pj] + d:
                        dist[i][j] = dist[pi][pj] + d
                        prev[i][j] = pi * N + pj
    
    # Return the shortest distance from the starting point to the south east corner
    return dist[M-1][N-1]

