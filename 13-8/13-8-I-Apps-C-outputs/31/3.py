
def is_symmetric(grid):
    # Check if the grid is symmetric
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def solve(H, W, S):
    # Initialize the grid with the given string
    grid = []
    for i in range(H):
        grid.append(list(S[i]))

    # Swap rows and columns of the grid to make it symmetric
    for i in range(H):
        for j in range(W):
            grid[i][j], grid[len(grid) - i - 1][len(grid[0]) - j - 1] = grid[len(grid) - i - 1][len(grid[0]) - j - 1], grid[i][j]

    # Check if the grid is symmetric
    if is_symmetric(grid):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(solve(H, W, S))

