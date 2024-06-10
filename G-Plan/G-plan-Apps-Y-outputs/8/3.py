
def count_dance_moves(N, M, grid):
    moves = 0
    prev_char = None
    
    for col in range(M):
        for row in range(N):
            if grid[row][col] == '$' and prev_char == '_':
                moves += 1
            prev_char = grid[row][col]
    
    return moves

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    
    dance_moves = count_dance_moves(N, M, grid)
    print(dance_moves)
