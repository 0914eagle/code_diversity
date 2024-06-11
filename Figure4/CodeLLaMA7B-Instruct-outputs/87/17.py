

def get_row(lst, x):
    
    # Initialize an empty list to store the coordinates
    coordinates = []

    # Iterate over the rows of the list
    for i, row in enumerate(lst):
        # Find the first occurrence of the integer x in the row
        column = row.index(x) if x in row else None
        # If x is found, add the coordinate to the list
        if column is not None:
            coordinates.append((i, column))

    # Sort the coordinates initially by rows in ascending order
    coordinates.sort(key=lambda x: x[0])

    # Sort the coordinates of each row by columns in descending order
    for row in coordinates:
        row.sort(key=lambda x: x[1], reverse=True)

    return coordinates

