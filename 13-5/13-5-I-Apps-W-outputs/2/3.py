
def solve(bomb_coordinates, bomb_states, cord_ranges):
    # Initialize a set to store the indices of the bombs that are activated
    activated_bombs = set()

    # Iterate over the bomb coordinates and states
    for i, (coordinate, state) in enumerate(zip(bomb_coordinates, bomb_states)):
        # If the bomb is activated, add its index to the set of activated bombs
        if state == 1:
            activated_bombs.add(i)

    # Initialize a set to store the indices of the bombs that are deactivated
    deactivated_bombs = set(range(len(bomb_coordinates))) - activated_bombs

    # Initialize a list to store the cords that should be cut
    cords_to_cut = []

    # Iterate over the cord ranges
    for cord_range in cord_ranges:
        # Extract the start and end coordinates of the cord range
        start_coordinate, end_coordinate = cord_range

        # Find the indices of the bombs that are activated and deactivated within the cord range
        activated_bombs_in_range = [i for i in activated_bombs if start_coordinate <= bomb_coordinates[i] <= end_coordinate]
        deactivated_bombs_in_range = [i for i in deactivated_bombs if start_coordinate <= bomb_coordinates[i] <= end_coordinate]

        # If there are no activated bombs in the range, we can cut the cord
        if not activated_bombs_in_range:
            cords_to_cut.append(cord_range)

        # If there are no deactivated bombs in the range, we can cut the cord
        elif not deactivated_bombs_in_range:
            cords_to_cut.append(cord_range)

    # If all the bombs are deactivated, return -1
    if not activated_bombs:
        return -1

    # Return the list of cords that should be cut
    return cords_to_cut

