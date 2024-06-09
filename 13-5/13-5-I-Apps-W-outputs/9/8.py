
def get_max_logo_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area of sub-square inside the given sub-rectangle
    max_area = 0

    # Loop through the rows of the sub-rectangle
    for i in range(r1, r2 + 1):
        # Loop through the columns of the sub-rectangle
        for j in range(c1, c2 + 1):
            # Check if the current cell is part of a Nanosoft logo
            if picture[i][j] in ["R", "G", "B", "Y"]:
                # Get the area of the current sub-square
                area = (i - r1 + 1) * (j - c1 + 1)

                # Update the maximum area if necessary
                max_area = max(max_area, area)

    # Return the maximum area of sub-square inside the given sub-rectangle
    return max_area

