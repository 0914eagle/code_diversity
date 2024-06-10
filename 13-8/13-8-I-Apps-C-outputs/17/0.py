
def input_data():
    n = int(input())
    vertical_spec = [list(map(int, input().split())) for _ in range(n)]
    horizontal_spec = [list(map(int, input().split())) for _ in range(n)]
    return n, vertical_spec, horizontal_spec

def solve(n, vertical_spec, horizontal_spec):
    # Initialize the grid with all borders as unmarked
    grid = [[0] * (n+1) for _ in range(n+1)]
    
    # Fill in the vertical borders
    for i in range(n):
        for j in range(len(vertical_spec[i])):
            # If the specification is 0, skip this row
            if vertical_spec[i][j] == 0:
                continue
            # Find the starting position of the group
            start = j * (vertical_spec[i][j] + 1)
            # Mark the borders in this group as 1
            for k in range(start, start + vertical_spec[i][j]):
                grid[i][k] = 1
    
    # Fill in the horizontal borders
    for j in range(n):
        for i in range(len(horizontal_spec[j])):
            # If the specification is 0, skip this column
            if horizontal_spec[j][i] == 0:
                continue
            # Find the starting position of the group
            start = i * (horizontal_spec[j][i] + 1)
            # Mark the borders in this group as 1
            for k in range(start, start + horizontal_spec[j][i]):
                grid[k][j] = 1
    
    return grid

def output_data(grid):
    for row in grid:
        print(''.join(map(str, row)))

if __name__ == '__main__':
    n, vertical_spec, horizontal_spec = input_data()
    grid = solve(n, vertical_spec, horizontal_spec)
    output_data(grid)

