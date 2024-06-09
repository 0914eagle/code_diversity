
def is_rearrangement_possible(num_islands, current_statues, desired_statues):
    # Initialize a dictionary to map each statue to its current and desired island
    statue_map = {}
    for i in range(num_islands):
        if current_statues[i] != 0:
            statue_map[current_statues[i]] = (i, desired_statues[i])
    
    # Initialize a set to keep track of visited islands
    visited_islands = set()
    
    # Start from the island with the empty pedestal
    empty_pedestal_island = current_statues.index(0)
    visited_islands.add(empty_pedestal_island)
    
    # Loop until all statues are in the desired position
    while len(visited_islands) < num_islands:
        # Get the current statue on the empty pedestal island
        current_statue = current_statues[empty_pedestal_island]
        
        # If the current statue is not in the desired position, move it to the next island
        if current_statue != desired_statues[empty_pedestal_island]:
            # Get the next island in the cycle
            next_island = (empty_pedestal_island + 1) % num_islands
            
            # If the next island has not been visited, move the statue to the next island
            if next_island not in visited_islands:
                visited_islands.add(next_island)
                empty_pedestal_island = next_island
            
            # If the next island has been visited, move the statue to the desired position
            else:
                empty_pedestal_island = statue_map[current_statue][1]
        
        # If the current statue is in the desired position, move to the next island
        else:
            empty_pedestal_island = (empty_pedestal_island + 1) % num_islands
    
    # If all statues are in the desired position, return "YES", otherwise return "NO"
    if all(current_statues[i] == desired_statues[i] for i in range(num_islands)):
        return "YES"
    else:
        return "NO"

