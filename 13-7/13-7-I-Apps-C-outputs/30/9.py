
def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        # Check if the subgrid is monotonic
        for i in range(len(subgrid)):
            for j in range(i+1, len(subgrid)):
                if subgrid[i] > subgrid[j]:
                    return False
        return True

    def count_subgrids(grid):
        # Count the number of non-empty subgrids
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += 1
        return count

    def count_monotonic_subgrids(grid):
        # Count the number of monotonic subgrids
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_monotonic(grid[i][j]):
                    count += 1
        return count

    # Implement your solution here
    return count_monotonic_subgrids(grid)

