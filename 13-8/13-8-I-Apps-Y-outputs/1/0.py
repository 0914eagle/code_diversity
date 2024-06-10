
def dfs(grid, i, j, visited):
    # Base case: if the current cell is not land or we have visited it before, return
    if grid[i][j] != "L" or (i, j) in visited:
        return
    
    # Mark the current cell as visited
    visited.add((i, j))
    
    # Recursively explore the neighbors
    for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
        dfs(grid, x, y, visited)

def numIslands(grid):
    # Initialize the number of islands to 0
    num_islands = 0
    
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is land and we have not visited it before, perform a DFS
            if grid[i][j] == "L" and (i, j) not in visited:
                visited = set()
                dfs(grid, i, j, visited)
                num_islands += 1
    
    # Return the number of islands
    return num_islands

if __name__ == '__main__':
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]
    print(numIslands(grid))

