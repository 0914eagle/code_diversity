
def get_squared_distance(matrix, falls):
    # Initialize a dictionary to store the distance of each fall from the tree
    distances = {}

    # Iterate over each fall
    for fall in falls:
        # Get the row and column of the fall
        row, col = fall

        # Initialize the distance to the tree as infinity
        distance = float('inf')

        # Iterate over the matrix to find the nearest tree
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # If the current cell is a tree, calculate the distance from the fall
                if matrix[i][j] == 'x':
                    # Calculate the distance using the Pythagorean theorem
                    d = (i - row) ** 2 + (j - col) ** 2

                    # If the distance is less than the current minimum distance, update the minimum distance
                    if d < distance:
                        distance = d

        # Add the distance to the dictionary
        distances[fall] = distance

    # Return the dictionary of distances
    return distances

