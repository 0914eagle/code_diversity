
def count_polygons(R, C):
    # Initialize a list to store the polygons
    polygons = []

    # Loop through each row
    for i in range(R):
        # Loop through each column
        for j in range(C):
            # Check if the current cell is empty
            if grid[i][j] == 0:
                # If it is empty, check if it is possible to form a polygon
                if possible_polygon(grid, i, j):
                    # If it is possible, add it to the list of polygons
                    polygons.append((i, j))

    # Return the number of polygons
    return len(polygons)

def possible_polygon(grid, i, j):
    # Check if the current cell is empty
    if grid[i][j] == 0:
        # If it is empty, check if it is possible to form a polygon
        if possible_polygon_helper(grid, i, j, 1):
            # If it is possible, return True
            return True

    # If the current cell is not empty or it is not possible to form a polygon, return False
    return False

def possible_polygon_helper(grid, i, j, count):
    # Check if the current cell is empty
    if grid[i][j] == 0:
        # If it is empty, set the current cell to the current count
        grid[i][j] = count
        # Increment the count
        count += 1
        # Recursively call the function for the neighboring cells
        possible_polygon_helper(grid, i-1, j, count)
        possible_polygon_helper(grid, i+1, j, count)
        possible_polygon_helper(grid, i, j-1, count)
        possible_polygon_helper(grid, i, j+1, count)
        # Return True if the count is greater than 2
        return count > 2

    # If the current cell is not empty, return False
    return False

if __name__ == '__main__':
    R, C = map(int, input().split())
    grid = [[0] * C for _ in range(R)]
    print(count_polygons(R, C))

