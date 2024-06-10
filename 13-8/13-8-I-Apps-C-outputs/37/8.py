
def get_min_cost(n, m, black_rectangles):
    # Initialize a grid of size n x n with all cells set to 0
    grid = [[0] * n for _ in range(n)]

    # Loop through each black rectangle and update the grid
    for x1, y1, x2, y2 in black_rectangles:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] += 1

    # Initialize the minimum total cost to 0
    min_cost = 0

    # Loop through each cell in the grid
    for i in range(n):
        for j in range(n):
            # If the cell is not white, add its cost to the minimum total cost
            if grid[i][j] != 0:
                min_cost += grid[i][j]

    return min_cost

def main():
    n, m = map(int, input().split())
    black_rectangles = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        black_rectangles.append((x1, y1, x2, y2))
    print(get_min_cost(n, m, black_rectangles))

if __name__ == '__main__':
    main()

