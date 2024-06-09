
def solve(h, w, n, pattern, commands):
    # Initialize variables
    board = [[0] * w for _ in range(h)]
    marker = [0, 0]
    timestep = 0
    dry_timestep = -1

    # Fill the board with the pattern
    for i in range(h):
        for j in range(w):
            if pattern[i][j] == '#':
                board[i][j] = 1

    # Execute the commands
    for command in commands:
        timestep += 1
        if command[0] == 'up':
            marker[0] += command[1]
        elif command[0] == 'down':
            marker[0] -= command[1]
        elif command[0] == 'left':
            marker[1] -= command[1]
        elif command[0] == 'right':
            marker[1] += command[1]

        # Check if the marker has run dry
        if board[marker[0]][marker[1]] == 1:
            dry_timestep = timestep

    # Check if the marker can still draw the target drawing
    if dry_timestep != -1 and board == pattern:
        return [dry_timestep, dry_timestep]
    else:
        return [-1, -1]

