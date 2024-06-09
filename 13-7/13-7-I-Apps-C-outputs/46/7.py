
def reconstruct_arrows(N, K, a):
    # Initialize a dictionary to map each person to their next position
    person_to_next_position = {i: a[i-1] for i in range(1, N+1)}
    # Initialize a set to keep track of the visited positions
    visited_positions = set()
    # Initialize a list to store the arrows
    arrows = []

    # Iterate through the K signals
    for _ in range(K):
        # Iterate through the persons in the order they visited their positions
        for person in range(1, N+1):
            # Get the next position for the person
            next_position = person_to_next_position[person]
            # If the next position is not visited yet, add it to the visited positions set
            if next_position not in visited_positions:
                visited_positions.add(next_position)
                # Add the arrow from the current person to the next position
                arrows.append((person, next_position))
            # Update the person's next position to their current position
            person_to_next_position[person] = person

    # If not all positions were visited, return "Impossible"
    if len(visited_positions) != N:
        return "Impossible"

    # Return the arrows list
    return arrows

