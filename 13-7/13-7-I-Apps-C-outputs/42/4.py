
def get_max_flowers(field, initial_position):
    # Initialize variables
    max_flowers = 0
    current_position = initial_position
    visited_flowers = set()

    # Loop through the field
    for row in range(len(field)):
        for col in range(len(field[0])):
            # Check if the current position is valid and has not been visited before
            if (row, col) != current_position and (row, col) not in visited_flowers:
                # Check if the current position has more petals than the previous position
                if field[row][col] > field[current_position[0]][current_position[1]]:
                    # Update the maximum number of flowers visited
                    max_flowers += 1
                    # Update the current position and add it to the visited set
                    current_position = (row, col)
                    visited_flowers.add(current_position)

    return max_flowers

