

def minPath(grid, k):
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]

    # Loop through the rows and columns of the grid
    for i in range(1, len(grid)):
        for j in range(i, len(grid[i])):
            # If the current cell is part of the minimum path, skip it
            if grid[i][j] in min_path:
                continue

            # If the current cell is not part of the minimum path, check if it is part of a shorter path
            for path in min_path:
                # If the current cell is part of a shorter path, skip it
                if grid[i][j] == path:
                    break
            else:
                # If the current cell is not part of a shorter path, add it to the minimum path
                min_path.append(grid[i][j])

            # If the minimum path length is equal to k, return it
            if len(min_path) == k:
                return min_path

    # If the minimum path length is less than k, return it
    return min_path


