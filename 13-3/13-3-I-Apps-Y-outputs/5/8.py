
def get_min_islands(image):
    # Initialize variables
    rows, cols = len(image), len(image[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    # Loop through each cell in the image
    for i in range(rows):
        for j in range(cols):
            # If the cell is land and not visited, explore the island and count it
            if image[i][j] == "L" and not visited[i][j]:
                explore_island(image, visited, i, j)
                islands += 1

    return islands

def explore_island(image, visited, i, j):
    # Mark the current cell as visited
    visited[i][j] = True

    # Recursively explore the island in all four directions
    if i > 0 and image[i - 1][j] == "L" and not visited[i - 1][j]:
        explore_island(image, visited, i - 1, j)
    if i < len(image) - 1 and image[i + 1][j] == "L" and not visited[i + 1][j]:
        explore_island(image, visited, i + 1, j)
    if j > 0 and image[i][j - 1] == "L" and not visited[i][j - 1]:
        explore_island(image, visited, i, j - 1)
    if j < len(image[0]) - 1 and image[i][j + 1] == "L" and not visited[i][j + 1]:
        explore_island(image, visited, i, j + 1)

if __name__ == "__main__":
    image = [
        [input() for _ in range(int(input()))]
        for _ in range(int(input()))
    ]
    print(get_min_islands(image))

