
import sys

def primonimo(n, m, p, board):
    # Initialize the visited array
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # Initialize the queue with the starting position
    queue = [(0, 0)]
    
    # Initialize the count of moves
    count = 0
    
    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        row, col = queue.pop(0)
        
        # If the current position is already visited, skip it
        if visited[row][col]:
            continue
        
        # Mark the current position as visited
        visited[row][col] = True
        
        # Add the current position to the list of moves
        moves.append(board[row][col])
        
        # Increment the count of moves
        count += 1
        
        # If the current position is equal to p, wrap around to 1
        if board[row][col] == p:
            board[row][col] = 1
        
        # Add the neighbors of the current position to the queue
        if row > 0 and not visited[row-1][col]:
            queue.append((row-1, col))
        if row < n-1 and not visited[row+1][col]:
            queue.append((row+1, col))
        if col > 0 and not visited[row][col-1]:
            queue.append((row, col-1))
        if col < m-1 and not visited[row][col+1]:
            queue.append((row, col+1))
    
    # If all positions are visited and the last position is equal to p, return the list of moves
    if all(all(visited[i]) for i in range(n)) and board[n-1][m-1] == p:
        return moves
    
    # If no winning sequence exists, return -1
    return -1

n, m, p = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

moves = []
result = primonimo(n, m, p, board)
if result == -1:
    print(-1)
else:
    print(len(result))
    print(*result)

