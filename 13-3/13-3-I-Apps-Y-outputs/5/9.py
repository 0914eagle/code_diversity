
def get_min_islands(image):
    # Initialize variables
    rows, cols = len(image), len(image[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    islands = 0

    # Loop through each cell in the image
    for i in range(rows):
        for j in range(cols):
            # If the cell is not visited and is land, visit it and count the number of connected land cells
            if not visited[i][j] and image[i][j] == "L":
                count = 0
                dfs(image, visited, i, j, count)
                islands += 1

    return islands

def dfs(image, visited, i, j, count):
    # Base case: if the cell is not land, return
    if image[i][j] != "L":
        return

    # Mark the cell as visited
    visited[i][j] = True
    count += 1

    # Recursive case: visit the four neighbors of the current cell
    if i > 0 and not visited[i-1][j]:
        dfs(image, visited, i-1, j, count)
    if i < rows-1 and not visited[i+1][j]:
        dfs(image, visited, i+1, j, count)
    if j > 0 and not visited[i][j-1]:
        dfs(image, visited, i, j-1, count)
    if j < cols-1 and not visited[i][j+1]:
        dfs(image, visited, i, j+1, count)

if __name__ == '__main__':
    image = [
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L']
    ]
    print(get_min_islands(image))

