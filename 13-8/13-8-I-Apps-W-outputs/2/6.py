
def solve(n, m, cubes):
    # Initialize a 2D array to store the number of cubes on each square
    num_cubes = [[0] * n for _ in range(n)]
    
    # Count the number of cubes on each square
    for cube in cubes:
        num_cubes[cube[0] - 1][cube[1] - 1] += 1
    
    # Initialize a queue to store the moves
    queue = []
    
    # Add the first move to the queue
    queue.append((0, 0, 1))
    
    # Loop until the queue is empty
    while queue:
        # Get the current move
        current_move = queue.pop(0)
        row, col, num_moves = current_move
        
        # Check if the current move is the last move
        if num_moves == m:
            return row + 1
        
        # Get the number of cubes on the current square
        num_cubes_on_square = num_cubes[row][col]
        
        # Check if the current square has a cube
        if num_cubes_on_square == 0:
            continue
        
        # Remove the cube from the current square
        num_cubes[row][col] -= 1
        
        # Add the move to the queue
        queue.append((row, col, num_moves + 1))
        
        # Add the move to the queue for the adjacent squares
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= r < n and 0 <= c < n:
                queue.append((r, c, num_moves + 1))
    
    # If the queue is empty, return -1
    return -1

