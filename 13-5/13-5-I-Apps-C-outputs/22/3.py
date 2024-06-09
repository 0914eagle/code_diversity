
def escape_speed(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exit
    for route in all_routes(n, m, e, roads, exits, start_brothers):
        # Calculate the speed required to take this route
        speed = calculate_speed(route, start_police)
        
        # If the speed is less than the minimum speed, update the minimum speed
        if speed < min_speed:
            min_speed = speed
    
    # If the minimum speed is infinity, return "IMPOSSIBLE"
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

def all_routes(n, m, e, roads, exits, start):
    # Initialize an empty list to store all possible routes
    routes = []
    
    # Loop through all possible roads from the starting point
    for road in roads:
        # If the road is not blocked and leads to a highway exit, add it to the list of routes
        if not blocked(road, exits) and road[1] in exits:
            routes.append(road)
    
    return routes

def calculate_speed(route, start_police):
    # Initialize the speed as zero
    speed = 0
    
    # Loop through all roads in the route
    for i in range(len(route) - 1):
        # Calculate the distance between the current road and the next road
        distance = distance_between(route[i], route[i + 1])
        
        # Calculate the time it takes to travel this distance at the maximum speed
        time = distance / max_speed
        
        # If the police car is ahead of the brothers and will reach the current road before they do, add the time it takes the police car to travel this distance to the total time
        if start_police < route[i][0] and start_police + time > route[i][0]:
            time += (start_police + time - route[i][0]) / max_speed
        
        # Update the speed based on the total time and distance
        speed = max(speed, distance / time)
    
    return speed

def blocked(road, exits):
    # If the road is blocked by the police car, return True
    if road[1] in exits:
        return True
    else:
        return False

def distance_between(road1, road2):
    # Calculate the distance between the two roads
    return abs(road1[1] - road2[1])

def max_speed():
    # Return the maximum speed of the police car
    return 160

