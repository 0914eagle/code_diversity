
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    # Initialize a set to store the collected data nodes
    collected_nodes = set()
    # Initialize the current coordinate as (x_s, y_s)
    current_coord = (x_s, y_s)
    # Initialize the time spent as 0
    time_spent = 0

    while time_spent < t:
        # Generate all possible next coordinates
        next_coords = [(current_coord[0] - 1, current_coord[1]),
                       (current_coord[0] + 1, current_coord[1]),
                       (current_coord[0], current_coord[1] - 1),
                       (current_coord[0], current_coord[1] + 1)]
        # Filter out the coordinates that are not in the data nodes list
        next_coords = [coord for coord in next_coords if coord in data_nodes]
        # If there are no next coordinates, break the loop
        if not next_coords:
            break
        # Choose the coordinate with the minimum Manhattan distance from the current coordinate
        next_coord = min(next_coords, key=lambda coord: abs(coord[0] - current_coord[0]) + abs(coord[1] - current_coord[1]))
        # Add the next coordinate to the collected nodes set
        collected_nodes.add(next_coord)
        # Update the current coordinate and time spent
        current_coord = next_coord
        time_spent += 1

    # Return the size of the collected nodes set
    return len(collected_nodes)

