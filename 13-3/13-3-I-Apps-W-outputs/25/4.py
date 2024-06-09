
def can_visit_friend(n, m, teleports):
    # Initialize a set to store the points that can be reached using teleports
    reachable_points = set([0])
    
    # Iterate through the teleports
    for teleport in teleports:
        # If the teleport's location is in the set of reachable points
        if teleport[0] in reachable_points:
            # Add the teleport's limit to the set of reachable points
            reachable_points.add(teleport[1])
    
    # Return True if the friend's house is in the set of reachable points, False otherwise
    return m in reachable_points

