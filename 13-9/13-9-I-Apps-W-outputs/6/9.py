
def solve(n, k, road):
    # Check if the last sector contains a rock
    if road[-1] == '#':
        return "NO"

    # Initialize a set to store the safe sectors
    safe_sectors = set()

    # Add the first sector as safe
    safe_sectors.add(1)

    # Iterate through the road description
    for i in range(1, n):
        # Check if the current sector contains a rock
        if road[i] == '#':
            # If it does, return "NO"
            return "NO"
        # Add the current sector to the safe sectors set
        safe_sectors.add(i + 1)

    # Check if the last sector is safe
    if n in safe_sectors:
        return "YES"
    else:
        return "NO"

