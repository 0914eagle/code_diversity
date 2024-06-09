
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimal speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exit
    for route in all_routes(n, m, e, roads, exits, start_brothers):
        # Calculate the speed required to escape using the route
        speed = calculate_speed(route, start_police)
        
        # If the speed is less than the current minimal speed, update the minimal speed
        if speed < min_speed:
            min_speed = speed
    
    # If the minimal speed is infinity, return "IMPOSSIBLE"
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

def all_routes(n, m, e, roads, exits, start):
    # Initialize an empty list to store all possible routes
    routes = []
    
    # Loop through all possible roads from the starting point
    for road in roads:
        # If the road is connected to the starting point and not already in the list of routes, add it to the list of routes
        if road[0] == start and road not in routes:
            routes.append(road)
    
    # Return the list of routes
    return routes

def calculate_speed(route, start_police):
    # Initialize the speed required to escape as zero
    speed = 0
    
    # Loop through all roads in the route
    for i in range(len(route) - 1):
        # Calculate the distance between the current road and the next road
        distance = route[i + 1][2] - route[i][2]
        
        # Calculate the time required to travel the distance at the maximum speed of the brothers' car
        time = distance / 160
        
        # Calculate the time required to travel the distance at the maximum speed of the police car
        police_time = distance / 160
        
        # If the brothers' car can reach the next road before the police car, add the time required to travel the distance at the maximum speed of the brothers' car to the total speed required to escape
        if time < police_time:
            speed += time
        # Otherwise, return "IMPOSSIBLE"
        else:
            return "IMPOSSIBLE"
    
    # Return the total speed required to escape
    return speed

