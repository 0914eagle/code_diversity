
def can_reach_end(n, k, road):
    # Initialize a set to store the indices of sectors with rocks
    rocks = set()
    # Iterate through the road description
    for i, char in enumerate(road):
        # If the current sector has a rock, add its index to the set
        if char == "#":
            rocks.add(i)
    # Initialize a set to store the indices of sectors that Ksusha can reach
    reachable = set([0])
    # Iterate through the road description
    for i in range(n - 1):
        # Get the indices of the next sectors that Ksusha can reach
        next_reachable = set()
        for j in reachable:
            # If the current sector has no rocks, add the indices of the next sectors that Ksusha can reach to the set
            if j + 1 not in rocks:
                next_reachable.add(j + 1)
            # If Ksusha can jump k sectors, add the indices of the next sectors that Ksusha can reach to the set
            for k_ in range(1, k + 1):
                if j + k_ not in rocks:
                    next_reachable.add(j + k_)
        # Add the indices of the next sectors that Ksusha can reach to the set of reachable sectors
        reachable = reachable.union(next_reachable)
    # Return "YES" if Ksusha can reach the last sector, otherwise return "NO"
    return "YES" if n - 1 in reachable else "NO"

