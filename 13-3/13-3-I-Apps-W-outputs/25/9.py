
def can_visit_friend(n, m, teleports):
    # Initialize a set to store the points that can be reached using teleports
    reachable_points = set([0])
    
    # Iterate through the teleports
    for teleport in teleports:
        # Get the location and limit of the teleport
        location, limit = teleport
        
        # Check if the teleport is within the reachable points
        if location in reachable_points:
            # Add the limit to the reachable points
            reachable_points.add(limit)
    
    # Check if the friend's house is within the reachable points
    if m in reachable_points:
        return "YES"
    else:
        return "NO"

