
def read_input():
    n = int(input())
    vertical_groups = []
    for i in range(n):
        line = input().split()
        if line[0] == '0':
            vertical_groups.append([])
        else:
            vertical_groups.append([int(x) for x in line])
    horizontal_groups = []
    for i in range(n):
        line = input().split()
        if line[0] == '0':
            horizontal_groups.append([])
        else:
            horizontal_groups.append([int(x) for x in line])
    return n, vertical_groups, horizontal_groups

def solve(n, vertical_groups, horizontal_groups):
    # Initialize the grid with no bars
    grid = [[0] * (n+1) for _ in range(n+1)]
    
    # Fill in the vertical bars
    for i in range(n):
        for j in range(len(vertical_groups[i])):
            size = vertical_groups[i][j]
            # Find a suitable position for the bar
            for k in range(n+1 - size):
                if all(grid[i][k+x] == 0 for x in range(size)):
                    # Mark the bar
                    for x in range(size):
                        grid[i][k+x] = 1
                    break
    
    # Fill in the horizontal bars
    for j in range(n):
        for i in range(len(horizontal_groups[j])):
            size = horizontal_groups[j][i]
            # Find a suitable position for the bar
            for k in range(n+1 - size):
                if all(grid[k+x][j] == 0 for x in range(size)):
                    # Mark the bar
                    for x in range(size):
                        grid[k+x][j] = 1
                    break
    
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(str(x) for x in row))

if __name__ == '__main__':
    n, vertical_groups, horizontal_groups = read_input()
    grid = solve(n, vertical_groups, horizontal_groups)
    print_grid(grid)

