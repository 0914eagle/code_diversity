
def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        # Check if the subgrid is monotonic in both rows and columns
        return all(subgrid[i][j] < subgrid[i][j+1] for i in range(len(subgrid)) for j in range(len(subgrid[0])-1)) and all(subgrid[i][j] < subgrid[i+1][j] for i in range(len(subgrid)-1) for j in range(len(subgrid[0])))

    # Initialize the number of monotonic subgrids to 0
    num_monotonic_subgrids = 0

    # Iterate over all possible non-empty subsets of rows and columns
    for r in range(1, len(grid)+1):
        for c in range(1, len(grid[0])+1):
            # Iterate over all possible ways to choose r rows and c columns
            for rows in combinations(range(len(grid)), r):
                for cols in combinations(range(len(grid[0])), c):
                    # Create a subgrid by taking elements from the chosen rows and columns
                    subgrid = [[grid[i][j] for j in cols] for i in rows]
                    # If the subgrid is monotonic, increment the number of monotonic subgrids
                    if is_monotonic(subgrid):
                        num_monotonic_subgrids += 1

    return num_monotonic_subgrids

