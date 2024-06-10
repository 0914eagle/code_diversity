
def count_dance_moves(N, M, grid):
    moves = 0
    for col in zip(*grid):
        if any(col):
            if not moves or moves[-1] == '_':
                moves += 1
    return moves

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    result = count_dance_moves(N, M, grid)
    print(result)
