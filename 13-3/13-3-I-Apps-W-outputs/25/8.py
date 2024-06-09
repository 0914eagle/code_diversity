
def can_visit_friend(n, m, teleports):
    # Initialize a set to store the points that can be reached using teleports
    reachable_points = set([0])
    
    # Iterate through the teleports
    for teleport in teleports:
        # Check if the current teleport's location is in the reachable points set
        if teleport[0] in reachable_points:
            # Add the teleport's limit to the reachable points set
            reachable_points.add(teleport[1])
    
    # Check if the friend's house is in the reachable points set
    if m in reachable_points:
        return "YES"
    else:
        return "NO"

