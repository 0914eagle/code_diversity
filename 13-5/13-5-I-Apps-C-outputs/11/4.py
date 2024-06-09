
def is_rearrangement_possible(num_islands, current_statues, desired_statues):
    # Initialize a dictionary to map each statue to its current and desired island
    statue_map = {}
    for i in range(num_islands):
        if current_statues[i] != 0:
            statue_map[current_statues[i]] = (i, desired_statues[i])
    
    # Initialize a set to keep track of the islands that have been visited
    visited_islands = set()
    
    # Start at the island with the empty pedestal
    current_island = 0
    visited_islands.add(current_island)
    
    # Loop until all the statues are in the desired position
    while len(visited_islands) < num_islands:
        # Get the current statue on the current island
        current_statue = current_statues[current_island]
        
        # If the current statue is not in the desired position, move it to the desired island
        if current_statue != desired_statues[current_island]:
            # Get the island that the current statue is on
            current_statue_island = statue_map[current_statue][0]
            
            # Get the island that the current statue should be on
            desired_statue_island = statue_map[current_statue][1]
            
            # Move the statue from the current island to the desired island
            current_statues[current_island] = 0
            current_statues[desired_statue_island] = current_statue
            statue_map[current_statue] = (desired_statue_island, desired_statues[desired_statue_island])
        
        # Move to the next island
        current_island = (current_island + 1) % num_islands
        visited_islands.add(current_island)
    
    # Check if all the statues are in the desired position
    for i in range(num_islands):
        if current_statues[i] != desired_statues[i]:
            return "NO"
    
    return "YES"

