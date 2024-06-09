
def get_input():
    n, m, t, op = map(int, input().split())
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))
    return n, m, t, op, grid

def is_valid_section(grid, op, t):
    # Check if the section is valid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return False
    # Check if the section satisfies the target value
    if op == '-':
        if sum(grid[0]) - sum(grid[1]) != t:
            return False
    elif op == '+':
        if sum(grid[0]) + sum(grid[1]) != t:
            return False
    elif op == '*':
        if sum(grid[0]) * sum(grid[1]) != t:
            return False
    elif op == '/':
        if sum(grid[0]) / sum(grid[1]) != t:
            return False
    return True

def count_valid_ways(n, m, t, op, grid):
    # Initialize the number of valid ways to 0
    valid_ways = 0
    # Iterate over all possible assignments of digits to the section
    for assignment in itertools.product(range(1, n+1), repeat=m):
        # Create a copy of the grid with the current assignment
        grid_copy = [[0] * n for _ in range(n)]
        for i in range(m):
            grid_copy[grid[i][0]-1][grid[i][1]-1] = assignment[i]
        # Check if the section is valid with the current assignment
        if is_valid_section(grid_copy, op, t):
            valid_ways += 1
    return valid_ways

if __name__ == '__main__':
    n, m, t, op, grid = get_input()
    print(count_valid_ways(n, m, t, op, grid))

