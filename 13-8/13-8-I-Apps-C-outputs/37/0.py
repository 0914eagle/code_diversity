
def get_min_cost(grid_size, black_rectangles):
    # Initialize a grid of zeros
    grid = [[0] * grid_size for _ in range(grid_size)]

    # Fill in the grid with the black rectangles
    for rectangle in black_rectangles:
        x1, y1, x2, y2 = rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = 1

    # Calculate the minimum cost of painting each cell
    min_cost = [[0] * grid_size for _ in range(grid_size)]
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                min_cost[i][j] = 1
            else:
                min_cost[i][j] = min(min_cost[i - 1][j], min_cost[i][j - 1], min_cost[i - 1][j - 1]) + 1

    # Return the minimum cost of painting the whole grid
    return min_cost[grid_size - 1][grid_size - 1]

def main():
    grid_size, num_rectangles = map(int, input().split())
    black_rectangles = []
    for _ in range(num_rectangles):
        x1, y1, x2, y2 = map(int, input().split())
        black_rectangles.append((x1, y1, x2, y2))
    print(get_min_cost(grid_size, black_rectangles))

if __name__ == '__main__':
    main()

