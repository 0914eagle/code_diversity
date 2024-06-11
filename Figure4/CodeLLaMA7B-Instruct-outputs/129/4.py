

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Set the distance for the starting cell to 0
    distance[0][0] = 0

    # Create a set to keep track of the cells that are still eligible for the path
    eligible = set()

    # Add the starting cell to the eligible set
    eligible.add((0, 0))

    # Loop until the eligible set is empty
    while eligible:
        # Get the cell with the minimum distance
        cell = min(eligible, key=lambda x: distance[x[0]][x[1]])

        # Remove the cell from the eligible set
        eligible.remove(cell)

        # Get the row and column of the cell
        row, col = cell

        # Loop through the neighboring cells
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # Check if the neighboring cell is valid
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) != cell:
                    # Check if the neighboring cell is eligible for the path
                    if distance[i][j] == float('inf'):
                        # Calculate the distance to the neighboring cell
                        distance[i][j] = distance[row][col] + grid[i][j]

                        # Set the previous cell for the neighboring cell
                        previous[i][j] = cell

                        # Add the neighboring cell to the eligible set
                        eligible.add((i, j))

    # Create an empty list to store the values of the cells in the path
    path = []

    # Start at the end cell and trace back the path
    cell = (len(
