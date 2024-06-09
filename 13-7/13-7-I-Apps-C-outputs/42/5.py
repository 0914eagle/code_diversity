
def get_max_visited_flowers(field, initial_position, petals):
    # Initialize variables
    max_visited_flowers = 0
    current_position = initial_position
    visited_flowers = set()

    # Loop through each flower in the field
    for row in range(len(field)):
        for col in range(len(field[0])):
            # If the current flower has more petals than the previous flower and it is not in the visited set, add it to the visited set and increment the maximum visited flowers
            if field[row][col] > petals[current_position[0] - 1][current_position[1] - 1] and (row, col) not in visited_flowers:
                visited_flowers.add((row, col))
                max_visited_flowers += 1
                current_position = (row + 1, col + 1)
    
    return max_visited_flowers

