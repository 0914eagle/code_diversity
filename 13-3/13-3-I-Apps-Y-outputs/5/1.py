
def f1(r, c):
    # Initialize a 2D array to store the number of islands
    num_islands = [[0 for _ in range(c)] for _ in range(r)]
    
    # Loop through each row and column
    for i in range(r):
        for j in range(c):
            # If the current cell is land and not already part of an island, create a new island
            if image[i][j] == "L" and num_islands[i][j] == 0:
                num_islands[i][j] = 1
                dfs(i, j, num_islands)
    
    # Return the total number of islands
    return sum(sum(row) for row in num_islands)

def dfs(i, j, num_islands):
    # Base case: if the current cell is water or already part of an island, return
    if image[i][j] == "W" or num_islands[i][j] != 0:
        return
    
    # Mark the current cell as part of an island
    num_islands[i][j] = 1
    
    # Recursively explore the neighboring cells
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < r and 0 <= y < c:
            dfs(x, y, num_islands)

if __name__ == '__main__':
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    print(f1(r, c))

