
def f1(r, c, image):
    # Initialize a 2D array to store the number of islands
    num_islands = [[0 for _ in range(c)] for _ in range(r)]

    # Loop through each row and column
    for i in range(r):
        for j in range(c):
            # If the current cell is land and not already part of an island, create a new island
            if image[i][j] == "L" and num_islands[i][j] == 0:
                num_islands[i][j] = 1
                dfs(i, j, num_islands, image)

    # Return the total number of islands
    return sum(sum(row) for row in num_islands)

def dfs(i, j, num_islands, image):
    # Base case: if the current cell is not land, return
    if image[i][j] != "L":
        return

    # Mark the current cell as part of an island
    num_islands[i][j] = 1

    # Recursively explore the four neighbors
    if i > 0 and num_islands[i-1][j] == 0:
        dfs(i-1, j, num_islands, image)
    if j > 0 and num_islands[i][j-1] == 0:
        dfs(i, j-1, num_islands, image)
    if i < len(num_islands) - 1 and num_islands[i+1][j] == 0:
        dfs(i+1, j, num_islands, image)
    if j < len(num_islands[0]) - 1 and num_islands[i][j+1] == 0:
        dfs(i, j+1, num_islands, image)

if __name__ == '__main__':
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    print(f1(r, c, image))

