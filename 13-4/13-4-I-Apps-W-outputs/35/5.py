
def f1(r, n):
    # Initialize a 2D array to represent the grid
    grid = [[0] * 2 for _ in range(r)]
    
    # Set the first n cells as reclaimed by the first city
    for i in range(n):
        grid[i][0] = 1
    
    # Check if the first city can reclaim any more cells
    for i in range(n, r):
        if grid[i][0] == 0 and grid[i][1] == 0:
            return "WIN"
    
    # Check if the second city can reclaim any more cells
    for i in range(n):
        if grid[i][0] == 0 and grid[i][1] == 0:
            return "LOSE"
    
    # If both cities cannot reclaim any more cells, return "LOSE"
    return "LOSE"

def f2(r, n):
    # Initialize a 2D array to represent the grid
    grid = [[0] * 2 for _ in range(r)]
    
    # Set the first n cells as reclaimed by the first city
    for i in range(n):
        grid[i][0] = 1
    
    # Check if the second city can reclaim any more cells
    for i in range(n, r):
        if grid[i][1] == 0:
            return "WIN"
    
    # Check if the first city can reclaim any more cells
    for i in range(n):
        if grid[i][0] == 0:
            return "LOSE"
    
    # If both cities cannot reclaim any more cells, return "LOSE"
    return "LOSE"

if __name__ == '__main__':
    r, n = map(int, input().split())
    print(f1(r, n))
    print(f2(r, n))

