
def get_total_cost(rectangles):
    # Calculate the total cost of painting the entire grid white
    total_cost = 0
    for rectangle in rectangles:
        total_cost += rectangle[2] * rectangle[3]
    return total_cost

def solve(n, m, rectangles):
    # Initialize the grid with all cells set to white
    grid = [[0] * n for _ in range(n)]

    # Iterate through the rectangles and color them in black
    for rectangle in rectangles:
        for i in range(rectangle[0], rectangle[2] + 1):
            for j in range(rectangle[1], rectangle[3] + 1):
                grid[i][j] = 1

    # Calculate the minimum total cost of painting the entire grid white
    total_cost = get_total_cost(rectangles)

    # Return the minimum total cost
    return total_cost

def main():
    # Read the input data
    n, m = map(int, input().split())
    rectangles = []
    for _ in range(m):
        rectangles.append(list(map(int, input().split())))

    # Solve the problem
    result = solve(n, m, rectangles)

    # Output the result
    print(result)

if __name__ == '__main__':
    main()

