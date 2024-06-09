
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exit
    for route in all_routes(n, m, e, roads, exits, start_brothers):
        # Calculate the speed required to escape using the route
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
    # Initialize an empty list to store all routes
    routes = []
    
    # Loop through all possible roads from the starting point
    for road in roads:
        # If the road is not blocked and leads to a highway exit, add it to the list of routes
        if not blocked(road, start, exits) and road[1] in exits:
            routes.append(road)
    
    return routes

def calculate_speed(route, start_police):
    # Initialize the speed required to escape as zero
    speed = 0
    
    # Loop through all roads in the route
    for road in route:
        # Calculate the distance between the current road and the previous road
        distance = road[2]
        
        # If the distance is greater than the current speed, update the speed
        if distance > speed:
            speed = distance
    
    # Calculate the time required to travel the route
    time = speed / 3.6
    
    # Calculate the distance between the starting point and the police car
    distance = distance_between(start_police, route[0][0])
    
    # Calculate the time required to catch the police car
    catch_time = distance / 160
    
    # If the time required to travel the route plus the time required to catch the police car is less than the time required to travel the route, return "IMPOSSIBLE"
    if time + catch_time < time:
        return "IMPOSSIBLE"
    else:
        return speed

def blocked(road, start, exits):
    # If the road is blocked by the police car, return True
    if road[0] == start and road[1] in exits:
        return True
    else:
        return False

def distance_between(start, end):
    # Calculate the distance between the starting point and the end point
    distance = ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5
    
    return distance

