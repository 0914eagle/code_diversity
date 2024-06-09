
def solve(N, M, cubes):
    # Initialize a 2D array to store the number of cubes on each square
    num_cubes = [[0] * N for _ in range(N)]
    
    # Count the number of cubes on each square
    for r, c in cubes:
        num_cubes[r-1][c-1] += 1
    
    # Initialize a queue to store the squares to be processed
    queue = [(0, 0)]
    
    # Initialize a set to store the visited squares
    visited = set()
    
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop until the queue is empty
    while queue:
        # Get the current square from the queue
        r, c = queue.pop(0)
        
        # If the current square is not visited, mark it as visited and increment the number of moves
        if (r, c) not in visited:
            visited.add((r, c))
            moves += 1
            
            # If the current square has a cube, remove it and add the adjacent squares to the queue
            if num_cubes[r][c] > 0:
                num_cubes[r][c] -= 1
                for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= new_r < N and 0 <= new_c < N:
                        queue.append((new_r, new_c))
    
    # Return the number of moves
    return moves

