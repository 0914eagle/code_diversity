
def can_ksusha_reach_end(n, k, road):
    # Check if the first and last characters of the road are valid
    if road[0] == "#" or road[-1] == "#":
        return "NO"
    
    # Initialize a set to store the safe sectors
    safe_sectors = set()
    
    # Add the first sector as safe
    safe_sectors.add(1)
    
    # Iterate through the road
    for i in range(1, n):
        # Check if the current sector is safe
        if road[i] == "#":
            return "NO"
        
        # Add the current sector to the set of safe sectors
        safe_sectors.add(i)
        
        # Check if the next k sectors are safe
        for j in range(1, k+1):
            if i + j > n:
                break
            if road[i+j] == "#":
                return "NO"
            safe_sectors.add(i+j)
    
    # Check if the last sector is safe
    if road[-1] == "#":
        return "NO"
    
    # If all the sectors are safe, return "YES"
    return "YES"

