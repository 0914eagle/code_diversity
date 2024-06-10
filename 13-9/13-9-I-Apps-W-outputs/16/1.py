
def paint_pixel(grid, row, col):
    grid[row][col] = "B"

def check_square(grid, row, col):
    if grid[row][col] == "B" and grid[row+1][col] == "B" and grid[row][col+1] == "B" and grid[row+1][col+1] == "B":
        return True
    return False

def solve(grid, moves):
    for move in moves:
        row, col = move
        paint_pixel(grid, row, col)
        if check_square(grid, row, col):
            return move[0]
    return 0

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    grid = [["W"] * m for _ in range(n)]
    moves = []
    for _ in range(k):
        moves.append(tuple(map(int, input().split())))
    print(solve(grid, moves))

