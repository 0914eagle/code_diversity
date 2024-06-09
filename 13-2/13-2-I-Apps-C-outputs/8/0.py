
def count_polygons(rows, cols):
    # Initialize a list to store the polygons
    polygons = []
    
    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # Check if the current cell is empty
            if matrix[i][j] == 0:
                # If it is empty, check if it is a valid polygon
                if is_valid_polygon(matrix, i, j):
                    # If it is a valid polygon, add it to the list
                    polygons.append((i, j))
    
    # Return the number of polygons
    return len(polygons)

def is_valid_polygon(matrix, row, col):
    # Check if the current cell is empty
    if matrix[row][col] == 0:
        # If it is empty, check if it is a valid polygon
        if is_valid_polygon_helper(matrix, row, col, 1):
            # If it is a valid polygon, return True
            return True
    
    # If the current cell is not empty or it is not a valid polygon, return False
    return False

def is_valid_polygon_helper(matrix, row, col, size):
    # Check if the polygon is valid
    if size == rows * cols:
        # If the polygon is valid, return True
        return True
    
    # Check if the current cell is empty
    if matrix[row][col] == 0:
        # If it is empty, mark it as visited
        matrix[row][col] = 1
        # Recursively check if the polygon is valid in the next cell
        if is_valid_polygon_helper(matrix, row + 1, col, size + 1):
            # If it is valid, return True
            return True
        if is_valid_polygon_helper(matrix, row - 1, col, size + 1):
            # If it is valid, return True
            return True
        if is_valid_polygon_helper(matrix, row, col + 1, size + 1):
            # If it is valid, return True
            return True
        if is_valid_polygon_helper(matrix, row, col - 1, size + 1):
            # If it is valid, return True
            return True
    
    # If the current cell is not empty or it is not a valid polygon, return False
    return False

if __name__ == '__main__':
    rows, cols = map(int, input().split())
    matrix = [[0] * cols for _ in range(rows)]
    print(count_polygons(rows, cols))

