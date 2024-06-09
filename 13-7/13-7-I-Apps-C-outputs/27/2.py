
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rectangles = []

    # Loop through each row of the table
    for i in range(n):
        # Loop through each column of the table
        for j in range(m):
            # If the current cell is not part of a rectangle, check if it can be part of a rectangle
            if a[i][j] == 0:
                # Check if the current cell can be part of a rectangle
                rectangle = can_be_part_of_rectangle(a, i, j)
                if rectangle:
                    # If the current cell can be part of a rectangle, add it to the list of rectangles
                    rectangles.append(rectangle)
                    # Increase the number of changed cells
                    changed_cells += 1

    # Check if the number of changed cells is less than or equal to k
    if changed_cells <= k:
        # If the number of changed cells is less than or equal to k, return the number of changed cells
        return changed_cells
    else:
        # If the number of changed cells is greater than k, return -1
        return -1

# Function to check if a cell can be part of a rectangle
def can_be_part_of_rectangle(a, i, j):
    # Initialize variables
    rectangle = []
    value = a[i][j]

    # Check if the current cell is not already part of a rectangle
    if value == 0:
        # Check if the current cell is adjacent to any other cell in the same row
        for j in range(m):
            if a[i][j] == value:
                # If the current cell is adjacent to another cell in the same row, add it to the rectangle
                rectangle.append((i, j))
                break

        # Check if the current cell is adjacent to any other cell in the same column
        for i in range(n):
            if a[i][j] == value:
                # If the current cell is adjacent to another cell in the same column, add it to the rectangle
                rectangle.append((i, j))
                break

    # Return the rectangle if it is not empty, otherwise return None
    if rectangle:
        return rectangle
    else:
        return None

