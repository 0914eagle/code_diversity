

def get_row(lst, x):
    
    # Initialize an empty list to store the coordinates
    coordinates = []

    # Iterate over the rows of the list
    for i, row in enumerate(lst):
        # Find the column index of the first occurrence of x in the row
        try:
            col_index = row.index(x)
        # If x is not found in the row, continue to the next row
        except ValueError:
            continue
        # Add the coordinate (row index, column index) to the list
        coordinates.append((i, col_index))

    # Sort the coordinates initially by rows in ascending order
    coordinates.sort(key=lambda x: x[0])

    # Sort the coordinates of each row by columns in descending order
    for row in coordinates:
        row.sort(key=lambda x: x[1], reverse=True)

    return coordinates


