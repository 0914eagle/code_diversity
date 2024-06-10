
def solve(grid_size, black_rectangles):
    # Initialize a grid of zeros
    grid = [[0] * grid_size for _ in range(grid_size)]

    # Fill in the grid with the black rectangles
    for rectangle in black_rectangles:
        x1, y1, x2, y2 = rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = 1

    # Calculate the minimum total cost
    total_cost = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                total_cost += 1
            else:
                total_cost += min(i, j)

    return total_cost

def main():
    grid_size, num_rectangles = map(int, input().split())
    black_rectangles = []
    for _ in range(num_rectangles):
        black_rectangles.append(list(map(int, input().split())))
    print(solve(grid_size, black_rectangles))

if __name__ == '__main__':
    main()

