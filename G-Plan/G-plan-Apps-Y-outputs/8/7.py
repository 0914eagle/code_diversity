
def count_dance_moves(N, M, grid):
    moves = 0
    for col in range(M):
        prev_char = grid[0][col]
        for row in range(1, N):
            if prev_char == '$' and grid[row][col] == '_':
                moves += 1
            prev_char = grid[row][col]
    return moves

if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    print(count_dance_moves(N, M, grid))
