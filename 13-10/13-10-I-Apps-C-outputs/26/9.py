
def get_tour_length(grid):
    # Calculate the length of the tour
    tour_length = 0
    for i in range(len(grid) - 1):
        tour_length += abs(grid[i][0] - grid[i + 1][0]) + abs(grid[i][1] - grid[i + 1][1])
    return tour_length

def check_tour_constraints(grid):
    # Check if the tour satisfies the constraints
    for i in range(len(grid) - 1):
        if abs(grid[i][0] - grid[i + 1][0]) not in [2, 3] or abs(grid[i][1] - grid[i + 1][1]) not in [2, 3]:
            return False
    return True

def find_tour(grid):
    # Find a tour that satisfies the constraints
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                grid[i][j] = 1
                if check_tour_constraints(grid):
                    return grid
                grid[i][j] = 0
    return -1

def main():
    grid = [[0] * 3 for _ in range(2)]
    grid[0] = [1, 2, 3]
    grid[1] = [4, 5, 6]
    print(find_tour(grid))

if __name__ == '__main__':
    main()

