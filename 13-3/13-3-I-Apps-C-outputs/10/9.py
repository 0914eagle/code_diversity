
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
        
        # Check if the marker has run out of ink
        if board[y][x] == 1:
            return -1, -1
        
        # Mark the current cell on the board
        board[y][x] = 1
    
    # Check if the final pattern matches the target pattern
    if board != pattern:
        return -1, -1
    
    # Return the minimum and maximum time that the marker can run out of ink
    min_time = 0
    max_time = n
    for i in range(n):
        if board[y][x] == 0:
            min_time = i + 1
            break
    
    for i in range(n - 1, -1, -1):
        if board[y][x] == 0:
            max_time = i + 1
            break
    
    return min_time, max_time

