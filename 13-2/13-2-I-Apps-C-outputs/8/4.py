
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
                if possible_to_form_polygon(grid, i, j):
                    # If it is possible, add the polygon to the list
                    polygons.append((i, j))
    
    # Return the number of polygons
    return len(polygons)

def possible_to_form_polygon(grid, i, j):
    # Check if the current cell is empty
    if grid[i][j] == 0:
        # If it is empty, check if it is possible to form a polygon
        if possible_to_form_polygon_helper(grid, i, j):
            # If it is possible, return True
            return True
    
    # If the current cell is not empty or it is not possible to form a polygon, return False
    return False

def possible_to_form_polygon_helper(grid, i, j):
    # Check if the current cell is empty
    if grid[i][j] == 0:
        # If it is empty, set it to 1
        grid[i][j] = 1
        
        # Check if it is possible to form a polygon in the four directions
        if possible_to_form_polygon_helper(grid, i-1, j) and possible_to_form_polygon_helper(grid, i, j-1) and possible_to_form_polygon_helper(grid, i+1, j) and possible_to_form_polygon_helper(grid, i, j+1):
            # If it is possible, return True
            return True
    
    # If the current cell is not empty or it is not possible to form a polygon, return False
    return False

if __name__ == '__main__':
    R, C = map(int, input().split())
    grid = [[0] * C for _ in range(R)]
    print(count_polygons(R, C))

