

def get_row(lst, x):
    
    # Initialize an empty list to store the coordinates
    coordinates = []

    # Iterate over the rows of the list
    for i, row in enumerate(lst):
        # Check if the element x is in the current row
        if x in row:
            # Get the index of the element x in the current row
            col_index = row.index(x)
            # Add the coordinate (i, col_index) to the list of coordinates
            coordinates.append((i, col_index))

    # Sort the coordinates initially by rows in ascending order
    coordinates.sort(key=lambda x: x[0])

    # Sort the coordinates of each row by columns in descending order
    for row in coordinates:
        row.sort(key=lambda x: x[1], reverse=True)

    return coordinates

