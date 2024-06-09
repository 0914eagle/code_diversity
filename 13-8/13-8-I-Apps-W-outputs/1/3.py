
def is_rectangular_lair(contamination_levels):
    # Convert the contamination levels to a matrix
    matrix = [list(map(int, row)) for row in contamination_levels]

    # Find the maximum value in the matrix
    max_value = max(max(row) for row in matrix)

    # If the maximum value is 0, return "No"
    if max_value == 0:
        return "No"

    # Initialize a set to store the coordinates of the corners of the lair
    corners = set()

    # Iterate over the rows of the matrix
    for i in range(len(matrix)):
        # Iterate over the columns of the matrix
        for j in range(len(matrix[i])):
            # If the current cell has the maximum value, add its coordinates to the set of corners
            if matrix[i][j] == max_value:
                corners.add((i, j))

    # If there are less than 2 corners, return "No"
    if len(corners) < 2:
        return "No"

    # Initialize a set to store the coordinates of the sides of the lair
    sides = set()

    # Iterate over the corners of the lair
    for i in range(len(corners)):
        # Get the coordinates of the current corner
        corner1 = corners.pop()

        # If there are no more corners, break
        if not corners:
            break

        # Get the coordinates of the next corner
        corner2 = corners.pop()

        # Add the coordinates of the sides of the current corner to the set of sides
        sides.add((corner1[0], corner2[1]))
        sides.add((corner1[1], corner2[0]))
        sides.add((corner2[0], corner1[1]))
        sides.add((corner2[1], corner1[0]))

    # If there are less than 4 sides, return "No"
    if len(sides) < 4:
        return "No"

    # Initialize a set to store the coordinates of the cells inside the lair
    inside_cells = set()

    # Iterate over the sides of the lair
    for i in range(len(sides)):
        # Get the coordinates of the current side
        side1 = sides.pop()

        # If there are no more sides, break
        if not sides:
            break

        # Get the coordinates of the next side
        side2 = sides.pop()

        # Add the coordinates of the cells inside the current side to the set of inside cells
        for i in range(side1[0], side2[0] + 1):
            for j in range(side1[1], side2[1] + 1):
                inside_cells.add((i, j))

    # If there are fewer inside cells than outside cells, return "No"
    if len(inside_cells) < (len(matrix) * len(matrix[0])) - len(inside_cells):
        return "No"

    # Return "Yes"
    return "Yes"

