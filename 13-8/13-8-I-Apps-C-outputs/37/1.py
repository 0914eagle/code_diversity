
def get_min_cost(n, m, black_rectangles):
    # Initialize a grid of size n x n with all cells set to white
    grid = [[0] * n for _ in range(n)]

    # Loop through each black rectangle
    for rect in black_rectangles:
        # Get the coordinates of the bottom-left and top-right corners
        x1, y1, x2, y2 = rect

        # Loop through each cell in the rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # If the cell is not already set to black, set it to black
                if grid[i][j] == 0:
                    grid[i][j] = 1

    # Initialize the minimum total cost to 0
    min_cost = 0

    # Loop through each row of the grid
    for i in range(n):
        # Initialize the number of consecutive white cells to 0
        num_consecutive_white = 0

        # Loop through each cell in the row
        for j in range(n):
            # If the cell is white, increment the number of consecutive white cells
            if grid[i][j] == 0:
                num_consecutive_white += 1
            # If the cell is black, add the number of consecutive white cells to the minimum total cost
            else:
                min_cost += num_consecutive_white
                num_consecutive_white = 0

        # Add the number of consecutive white cells in the last row to the minimum total cost
        min_cost += num_consecutive_white

    return min_cost

def main():
    n, m = map(int, input().split())
    black_rectangles = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        black_rectangles.append([x1, y1, x2, y2])
    print(get_min_cost(n, m, black_rectangles))

if __name__ == '__main__':
    main()

