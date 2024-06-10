
def get_min_cost(grid_size, black_rectangles):
    # Initialize the cost array with 0s
    cost = [[0] * grid_size for _ in range(grid_size)]

    # Loop through each black rectangle
    for rect in black_rectangles:
        # Get the coordinates of the rectangle
        x1, y1, x2, y2 = rect

        # Loop through each cell in the rectangle
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # Increment the cost of the cell by 1
                cost[i][j] += 1

    # Return the maximum cost in the cost array
    return max(max(row) for row in cost)

def main():
    grid_size, num_black_rectangles = map(int, input().split())
    black_rectangles = []

    for _ in range(num_black_rectangles):
        black_rectangles.append(list(map(int, input().split())))

    print(get_min_cost(grid_size, black_rectangles))

if __name__ == '__main__':
    main()

