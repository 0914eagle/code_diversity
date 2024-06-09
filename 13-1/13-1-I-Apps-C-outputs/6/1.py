
def solve(n_r, n_c, n, m, files):
    # Initialize a grid to represent the screen
    grid = [[0] * n_c for _ in range(n_r)]

    # Populate the grid with the files to be deleted
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        grid[r][c] = 1

    # Initialize a variable to store the minimum number of moves
    min_moves = float('inf')

    # Iterate over all possible combinations of files to be deleted
    for i in range(1 << n):
        # Initialize a variable to store the number of moves
        moves = 0

        # Iterate over all files in the current combination
        for j in range(n):
            # Check if the file is set in the current combination
            if i & (1 << j):
                # Get the row and column of the file
                r, c = files[j * 2], files[j * 2 + 1]

                # Check if the file is already in the correct position
                if grid[r][c] == 1:
                    continue

                # Find the closest empty space for the file
                empty_r, empty_c = find_empty_space(grid, r, c)

                # Update the grid with the new position of the file
                grid[empty_r][empty_c] = 1
                grid[r][c] = 0

                # Increment the number of moves
                moves += 1

        # Check if the current combination has the minimum number of moves
        if moves < min_moves:
            min_moves = moves

    return min_moves

def find_empty_space(grid, r, c):
    # Initialize a variable to store the closest empty space
    closest_empty_r, closest_empty_c = None, None

    # Iterate over the rows and columns of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current position is empty
            if grid[i][j] == 0:
                # Calculate the distance between the current position and the file
                distance = abs(i - r) + abs(j - c)

                # Check if the current position is closer than the previous closest empty space
                if closest_empty_r is None or distance < closest_empty_r:
                    closest_empty_r, closest_empty_c = i, j

    return closest_empty_r, closest_empty_c

n_r, n_c, n, m = map(int, input().split())
files = [int(x) for x in input().split()]
print(solve(n_r, n_c, n, m, files))

