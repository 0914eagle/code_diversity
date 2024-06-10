
def solve(n, vertical_spec, horizontal_spec):
    # Initialize the grid with 0s
    grid = [[0] * (n + 1) for _ in range(n)]
    
    # Fill in the vertical bars
    for i, spec in enumerate(vertical_spec):
        for j in range(spec):
            # Find the first available position in the row
            for k in range(n + 1):
                if grid[i][k] == 0:
                    grid[i][k] = 1
                    break
    
    # Fill in the horizontal bars
    for j, spec in enumerate(horizontal_spec):
        for i in range(spec):
            # Find the first available position in the column
            for k in range(n):
                if grid[k][j] == 0:
                    grid[k][j] = 1
                    break
    
    # Return the grid as a list of strings
    return [''.join(map(str, row)) for row in grid]

def main():
    n = int(input())
    vertical_spec = [list(map(int, input().split())) for _ in range(n)]
    horizontal_spec = [list(map(int, input().split())) for _ in range(n)]
    solution = solve(n, vertical_spec, horizontal_spec)
    print('\n'.join(solution))

if __name__ == '__main__':
    main()

