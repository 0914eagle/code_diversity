
def is_rearrangement_possible(n, a, b):
    # Initialize a dictionary to map each statue to its current and desired island
    statue_map = {statue: (current_island, desired_island) for current_island, statue in enumerate(a, 1) for desired_island in range(n) if b[desired_island] == statue}

    # Initialize a set to keep track of the islands that have been visited
    visited_islands = set()

    # Initialize a variable to keep track of the current island
    current_island = 1

    # Loop until all islands have been visited
    while len(visited_islands) < n:
        # Get the statue on the current island
        statue = a[current_island - 1]

        # If the statue is not zero, it is a valid statue that can be moved
        if statue != 0:
            # Get the current and desired island for the statue
            current_island, desired_island = statue_map[statue]

            # If the desired island has not been visited, move the statue to the desired island
            if desired_island not in visited_islands:
                visited_islands.add(desired_island)
                current_island = desired_island

        # Move to the next island
        current_island = (current_island + 1) % n

    # If all islands have been visited, return "YES", otherwise return "NO"
    return "YES" if len(visited_islands) == n else "NO"

