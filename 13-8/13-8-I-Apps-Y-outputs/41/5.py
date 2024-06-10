
def is_objective_achievable(grid):
    
    # Initialize a set to store the indices of the squares that need to be painted black
    squares_to_paint = set()

    # Loop through the grid and find the indices of the squares that need to be painted black
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                squares_to_paint.add((i, j))

    # Initialize a set to store the indices of the squares that have been painted
    painted_squares = set()

    # Loop through the grid and find the indices of the squares that have been painted
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                painted_squares.add((i, j))

    # Initialize a set to store the indices of the squares that are horizontally or vertically adjacent to a painted square
    adjacent_squares = set()

    # Loop through the grid and find the indices of the squares that are horizontally or vertically adjacent to a painted square
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in painted_squares:
                if i > 0 and (i - 1, j) in painted_squares:
                    adjacent_squares.add((i - 1, j))
                if i < len(grid) - 1 and (i + 1, j) in painted_squares:
                    adjacent_squares.add((i + 1, j))
                if j > 0 and (i, j - 1) in painted_squares:
                    adjacent_squares.add((i, j - 1))
                if j < len(grid[i]) - 1 and (i, j + 1) in painted_squares:
                    adjacent_squares.add((i, j + 1))

    # Check if all the squares that need to be painted black are in the set of adjacent squares
    return squares_to_paint.issubset(adjacent_squares)

def read_grid():
    
    grid = []
    for _ in range(int(input())):
        grid.append(list(input()))
    return grid

def main():
    grid = read_grid()
    print("Yes" if is_objective_achievable(grid) else "No")

if __name__ == '__main__':
    main()

