
def get_min_cost(n, m, black_rectangles):
    # Initialize a grid of size n x n with all cells set to 0
    grid = [[0] * n for _ in range(n)]

    # Iterate over the black rectangles
    for x1, y1, x2, y2 in black_rectangles:
        # Update the grid with the cost of each cell in the rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] += 1

    # Find the minimum cost in the grid
    min_cost = float('inf')
    for i in range(n):
        for j in range(n):
            min_cost = min(min_cost, grid[i][j])

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

