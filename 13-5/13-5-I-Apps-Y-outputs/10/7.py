
def get_least_time(intersections, streets, start_intersection, end_intersection, start_time, mister_george_route):
    # Initialize a dictionary to store the time it takes to reach each intersection
    intersection_time = {intersection: float('inf') for intersection in intersections}
    intersection_time[start_intersection] = 0
    
    # Initialize a set to store the intersections that have been visited
    visited_intersections = set()
    
    # Loop through each intersection in the route
    for intersection in mister_george_route:
        # If the intersection has been visited, skip it
        if intersection in visited_intersections:
            continue
        # Mark the intersection as visited
        visited_intersections.add(intersection)
        # Get the time it takes to reach the next intersection
        next_intersection_time = intersection_time[intersection] + streets[(intersection, mister_george_route[intersection])]['time']
        # If the next intersection is the end intersection, return the time
        if intersection == end_intersection:
            return next_intersection_time
        # Update the time it takes to reach the next intersection
        intersection_time[mister_george_route[intersection]] = next_intersection_time
    
    # If the end intersection has not been reached, return -1
    return -1

