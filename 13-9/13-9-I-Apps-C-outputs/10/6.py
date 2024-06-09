
def solve(matrix, falls):
    # Initialize a dictionary to store the distances for each fall
    distances = {}

    # Loop through each fall
    for fall in falls:
        # Get the row and column of the fall
        row, col = fall

        # Initialize the minimum distance to a large value
        min_distance = 1000

        # Loop through each tree in the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # If the tree is not at the fall location, calculate the distance between the tree and the fall
                if matrix[i][j] == "x" and (i, j) != (row, col):
                    distance = ((i - row) ** 2 + (j - col) ** 2) ** 0.5

                    # If the distance is smaller than the current minimum distance, update the minimum distance
                    if distance < min_distance:
                        min_distance = distance

        # Add the minimum distance to the dictionary with the fall as the key
        distances[fall] = min_distance ** 2

    # Return the dictionary of distances
    return distances

