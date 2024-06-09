
def reconstruct_arrows(N, K, a):
    # Initialize a dictionary to map each person to their next position
    person_to_next_position = {}
    for i in range(N):
        person_to_next_position[i+1] = a[i]

    # Initialize a set to keep track of the visited positions
    visited_positions = set()

    # Initialize a list to store the arrows
    arrows = []

    # Loop through each person and their next position
    for person, next_position in person_to_next_position.items():
        # If the next position is not in the visited positions, add it to the visited positions set
        if next_position not in visited_positions:
            visited_positions.add(next_position)
            # Add the arrow from the current person to the next position
            arrows.append((person, next_position))
        # If the next position is already in the visited positions, add the arrow from the current person to the next position's next position
        else:
            while next_position in visited_positions:
                next_position = person_to_next_position[next_position]
            visited_positions.add(next_position)
            arrows.append((person, next_position))

    # If the number of arrows is not equal to the number of people, return "Impossible"
    if len(arrows) != N:
        return "Impossible"

    # Otherwise, return the arrows in the order they were added
    return [arrow[1] for arrow in arrows]

