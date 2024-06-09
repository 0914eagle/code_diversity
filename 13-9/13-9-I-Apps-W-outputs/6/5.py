
def ksusha_and_the_road(n, k, road):
    # Check if the first and last characters are both ".", indicating that there are no rocks at the beginning and end of the road
    if road[0] != "." or road[-1] != ".":
        return "NO"
    
    # Initialize a set to store the indices of the sectors that Ksusha can reach
    reachable_sectors = set([0])
    
    # Iterate through the road description
    for i in range(1, n):
        # If the current sector contains a rock, skip it
        if road[i] == "#":
            continue
        
        # Add the indices of the sectors that Ksusha can reach to the set
        reachable_sectors |= set(range(i - k, i + 1))
    
    # Check if the last sector is reachable
    if n - 1 in reachable_sectors:
        return "YES"
    else:
        return "NO"

