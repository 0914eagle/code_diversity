
def solve(n, a, b):
    # Initialize a dictionary to map each statue to its current and desired island
    statue_map = {i: (a[i], b[i]) for i in range(n)}
    
    # Initialize a set to keep track of the islands that have been visited
    visited_islands = set()
    
    # Initialize a variable to keep track of the current island
    current_island = 0
    
    # Loop until all the islands have been visited
    while len(visited_islands) < n:
        # Get the statue and its desired island for the current island
        statue, desired_island = statue_map[current_island]
        
        # If the current island has a statue and it is not on the desired island, move the statue
        if statue and current_island != desired_island:
            # Get the statue and its current island for the desired island
            desired_statue, desired_current_island = statue_map[desired_island]
            
            # If the desired island has no statue or the statue on the desired island is not the current statue, move the statue
            if not desired_statue or desired_statue != statue:
                # Update the dictionary to reflect the movement
                statue_map[current_island] = (0, desired_island)
                statue_map[desired_island] = (statue, current_island)
                
                # Add the current island to the set of visited islands
                visited_islands.add(current_island)
                
                # Set the current island to the desired island
                current_island = desired_island
            else:
                # If the desired island has the current statue, move on to the next island
                current_island = desired_current_island
        else:
            # If the current island has no statue or it is on the desired island, move on to the next island
            current_island = desired_island
    
    # If all the islands have been visited, return "YES"
    if len(visited_islands) == n:
        return "YES"
    else:
        return "NO"

