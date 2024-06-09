
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exit
    for route in permutations(range(1, n+1)):
        # If the route does not include the police car's starting point, skip it
        if start_police not in route:
            continue
        
        # Initialize the current speed as 0 km/h
        current_speed = 0
        
        # Loop through each section of the route
        for i in range(len(route)-1):
            # Find the road between the current and next intersection
            road = next((r for r in roads if r[0] == route[i] and r[1] == route[i+1]), None)
            
            # If the road is not found, the route is not possible
            if road is None:
                break
            
            # Calculate the time it takes to travel the length of the road at the current speed
            time = road[2] / current_speed
            
            # Calculate the acceleration needed to reach the maximum speed in the time available
            acceleration = (road[3] - current_speed) / time
            
            # Update the current speed based on the acceleration and time
            current_speed += acceleration * time
            
            # If the current speed exceeds the maximum speed, the route is not possible
            if current_speed > road[3]:
                break
        
        # If the route is possible and the current speed is less than the minimum speed required to escape, update the minimum speed
        if current_speed < min_speed:
            min_speed = current_speed
    
    # If the minimum speed is infinity, it is impossible to escape
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    
    # Otherwise, return the minimum speed required to escape
    return min_speed

