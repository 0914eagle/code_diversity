
def get_valid_colorings(n, a):
    # Initialize a 2D array to store the colorings
    colorings = [[0] * n for _ in range(n)]

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(n):
            # If the current cell is not colored, skip it
            if colorings[i][j] == 0:
                continue

            # If the current cell is colored, check if it forms a valid loop
            if not is_valid_loop(i, j, colorings):
                # If it doesn't form a valid loop, return 0
                return 0

    # If all cells form valid loops, return 1
    return 1

def is_valid_loop(i, j, colorings):
    # If the current cell is not colored, return True
    if colorings[i][j] == 0:
        return True

    # If the current cell is colored, check if it forms a valid loop
    color = colorings[i][j]
    visited = set()
    queue = [(i, j)]

    while queue:
        # Pop a cell from the queue
        i, j = queue.pop(0)

        # If the cell is already visited, skip it
        if (i, j) in visited:
            continue

        # Mark the cell as visited
        visited.add((i, j))

        # If the cell is not colored, return False
        if colorings[i][j] == 0:
            return False

        # If the cell is colored and its color is not the same as the current color, return False
        if colorings[i][j] != color:
            return False

        # Add the neighboring cells to the queue
        for neighbor in get_neighbors(i, j, colorings):
            queue.append(neighbor)

    # If all cells form a valid loop, return True
    return True

def get_neighbors(i, j, colorings):
    # Get the number of rows and columns
    n = len(colorings)

    # Initialize a list to store the neighbors
    neighbors = []

    # Check if the current cell has a neighbor in the top row
    if i > 0 and colorings[i - 1][j] != 0:
        neighbors.append((i - 1, j))

    # Check if the current cell has a neighbor in the bottom row
    if i < n - 1 and colorings[i + 1][j] != 0:
        neighbors.append((i + 1, j))

    # Check if the current cell has a neighbor in the left column
    if j > 0 and colorings[i][j - 1] != 0:
        neighbors.append((i, j - 1))

    # Check if the current cell has a neighbor in the right column
    if j < n - 1 and colorings[i][j + 1] != 0:
        neighbors.append((i, j + 1))

    return neighbors

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(get_valid_colorings(n, a))

if __name__ == "__main__":
    main()

