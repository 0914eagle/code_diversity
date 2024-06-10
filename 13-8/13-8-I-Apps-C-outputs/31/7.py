
def is_symmetric(grid):
    # Check if the grid is symmetric by comparing the elements in the top row with the elements in the bottom row, and the elements in the left column with the elements in the right column
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def can_make_symmetric(grid):
    # Check if the grid can be made symmetric by swapping two rows or two columns
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            if grid[i] != grid[j] and is_symmetric(swap_rows(grid, i, j)):
                return True
            elif grid[:, i] != grid[:, j] and is_symmetric(swap_cols(grid, i, j)):
                return True
    return False

def swap_rows(grid, i, j):
    # Swap the ith row with the jth row of the grid
    grid[i], grid[j] = grid[j], grid[i]
    return grid

def swap_cols(grid, i, j):
    # Swap the ith column with the jth column of the grid
    grid = grid.T
    grid[i], grid[j] = grid[j], grid[i]
    return grid.T

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print("YES") if can_make_symmetric(grid) else print("NO")

