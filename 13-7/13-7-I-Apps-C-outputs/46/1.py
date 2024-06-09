
def reconstruct_arrows(N, K, arrows):
    # Initialize a dictionary to map each person to their next position
    person_to_next_position = {}
    for i in range(N):
        person_to_next_position[i+1] = arrows[i]

    # Initialize a set to keep track of the visited positions
    visited_positions = set()

    # Initialize a list to store the final arrow placement
    arrow_placement = []

    # Iterate through each person and their next position
    for i in range(N):
        # Get the current person and their next position
        person = i+1
        next_position = person_to_next_position[person]

        # If the next position has not been visited before, add it to the visited positions set
        if next_position not in visited_positions:
            visited_positions.add(next_position)
        # If the next position has been visited before, find the previous position that leads to it
        else:
            # Iterate through the visited positions to find the previous position that leads to the next position
            for j in range(N):
                if person_to_next_position[j+1] == next_position:
                    # Add the arrow from the previous position to the current position
                    arrow_placement.append(j+1)
                    break

    # If the number of visited positions is not equal to the number of people, the arrow placement is impossible
    if len(visited_positions) != N:
        return "Impossible"

    # Return the final arrow placement
    return arrow_placement

