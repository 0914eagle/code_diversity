
def solve(h, w, n, pattern, commands):
    # Initialize the board and the current position of the marker
    board = [[0] * w for _ in range(h)]
    x, y = 0, 0
    
    # Parse the commands and execute them one by one
    for command in commands:
        direction, distance = command.split()
        distance = int(distance)
        if direction == "up":
            y -= distance
        elif direction == "down":
            y += distance
        elif direction == "left":
            x -= distance
        elif direction == "right":
            x += distance
        
        # Check if the marker has run dry
        if board[y][x] == 1:
            return [-1, -1]
        
        # Mark the current cell on the board
        board[y][x] = 1
    
    # Check if the final pattern matches the target pattern
    if board != pattern:
        return [-1, -1]
    
    # Return the minimum and maximum time that the marker can run dry
    min_time = max_time = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                min_time = max(min_time, j)
                max_time = max(max_time, j)
    
    return [min_time, max_time]

