
def get_total_cost(black_rectangles):
    # Initialize a grid of size n x n with all cells white
    grid = [[0] * n for _ in range(n)]

    # Loop through all black rectangles
    for rect in black_rectangles:
        # Get the coordinates of the bottom-left and top-right corners of the rectangle
        x1, y1, x2, y2 = rect

        # Loop through all cells in the rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # If the cell is not already white, color it black and add the cost to the total cost
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    total_cost += min(x2 - x1 + 1, y2 - y1 + 1)

    return total_cost

def main():
    n, m = map(int, input().split())
    black_rectangles = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        black_rectangles.append([x1, y1, x2, y2])

    print(get_total_cost(black_rectangles))

if __name__ == '__main__':
    main()

