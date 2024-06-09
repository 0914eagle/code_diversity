
def get_island_count(image):
    # Initialize a 2D array to store the number of islands
    island_count = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    # Loop through each cell in the image
    for i in range(len(image)):
        for j in range(len(image[0])):
            # If the current cell is land and it has not been visited before, visit all the adjacent cells that are also land and mark them as visited
            if image[i][j] == "L" and island_count[i][j] == 0:
                dfs(image, i, j, island_count)

    # Return the total number of islands
    return sum(sum(row) for row in island_count)

def dfs(image, i, j, island_count):
    # Mark the current cell as visited
    island_count[i][j] = 1

    # Recursively visit all adjacent cells that are also land
    for row, col in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == "L" and island_count[row][col] == 0:
            dfs(image, row, col, island_count)

if __name__ == "__main__":
    image = [
        [ "L", "L", "L", "L", "L" ],
        [ "L", "L", "L", "L", "L" ],
        [ "L", "L", "L", "L", "L" ],
        [ "L", "L", "L", "L", "L" ]
    ]
    print(get_island_count(image))

