
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

            # Get the color of the current cell
            color = colorings[i][j]

            # Loop through the neighbors of the current cell
            for neighbor in get_neighbors(i, j, n):
                # If the neighbor is not colored, skip it
                if colorings[neighbor[0]][neighbor[1]] == 0:
                    continue

                # If the neighbor has a different color, return 0
                if colorings[neighbor[0]][neighbor[1]] != color:
                    return 0

    # If all the conditions are met, return 1
    return 1

# Function to get the neighbors of a cell
def get_neighbors(i, j, n):
    neighbors = []

    # Top row
    if i > 0:
        neighbors.append((i-1, j))

    # Bottom row
    if i < n-1:
        neighbors.append((i+1, j))

    # Left column
    if j > 0:
        neighbors.append((i, j-1))

    # Right column
    if j < n-1:
        neighbors.append((i, j+1))

    return neighbors

# Main function
def main():
    # Read the input
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    # Get the valid colorings
    valid_colorings = get_valid_colorings(n, a)

    # Print the number of valid colorings
    print(valid_colorings)

if __name__ == "__main__":
    main()

