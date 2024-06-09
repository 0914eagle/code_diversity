
def solve(h, w, n, pattern, commands):
    # Initialize the board and the current position of the marker
    board = [[0] * w for _ in range(h)]
    x, y = 0, 0
    
    # Iterate through the commands and execute them one by one
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
        
        # Mark the current position on the board
        board[y][x] = 1
    
    # Check if the final pattern matches the target pattern
    if board != pattern:
        return [-1, -1]
    
    # Find the earliest and latest time the marker can run dry
    earliest = 0
    latest = n
    for i in range(n):
        if board[y][x] == 0:
            earliest = i + 1
            break
        if direction == "up":
            y -= 1
        elif direction == "down":
            y += 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
    
    for i in range(n-1, -1, -1):
        if board[y][x] == 0:
            latest = i
            break
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        elif direction == "left":
            x += 1
        elif direction == "right":
            x -= 1
    
    return [earliest, latest]

