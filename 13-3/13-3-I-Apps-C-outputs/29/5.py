
def primonimo(board):
    # Initialize variables
    n, m, p = board[0]
    moves = []
    visited = set()
    queue = [(0, 0)]

    # Loop through the queue
    while queue:
        # Get the current position
        row, col = queue.pop(0)

        # Check if the current position is already visited
        if (row, col) in visited:
            continue

        # Mark the current position as visited
        visited.add((row, col))

        # Add the current position to the moves list
        moves.append(board[row][col])

        # Check if all squares show p
        if len(moves) == p * m * n:
            return moves

        # Add the neighbors to the queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < n and 0 <= c < m:
                queue.append((r, c))

    # If no winning sequence exists, return -1
    return -1

