
def can_ksusha_reach_end(n, k, road):
    # Check if the first and last characters are "."
    if road[0] != "." or road[-1] != ".":
        return "NO"
    
    # Initialize a set to store the safe sectors
    safe_sectors = set([1])
    
    # Iterate through the road description
    for i in range(1, n):
        # If the current sector is safe and there is a jump of length k or less to the next sector, add the next sector to the safe sectors set
        if road[i] == "." and i + k <= n:
            safe_sectors.add(i + 1)
    
    # Check if the last sector is safe
    if road[-1] == ".":
        safe_sectors.add(n)
    
    # Return "YES" if all sectors are safe, otherwise return "NO"
    return "YES" if len(safe_sectors) == n else "NO"

