
def can_reach_end(n, k, road):
    # Initialize a set to store the indices of sectors with rocks
    rocks = set()
    # Iterate through the road description
    for i, sector in enumerate(road):
        # If the current sector has a rock, add its index to the set
        if sector == "#":
            rocks.add(i)
    # Initialize a set to store the indices of sectors that Ksusha can reach
    reachable = set([0])
    # Iterate through the road description
    for i in range(n - 1):
        # Get the indices of the sectors that Ksusha can reach in the current step
        next_reachable = set()
        for j in reachable:
            # If Ksusha can reach sector j, she can also reach sector j + 1, j + 2, ..., j + k
            for k in range(1, k + 1):
                if j + k not in rocks and j + k <= n - 1:
                    next_reachable.add(j + k)
        # Add the indices of the sectors that Ksusha can reach in the current step to the set
        reachable = reachable.union(next_reachable)
    # If Ksusha can reach the last sector, return "YES", otherwise return "NO"
    if n - 1 in reachable:
        return "YES"
    else:
        return "NO"

