
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinite
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exits
    for exit in exits:
        # Calculate the distance from the brothers' starting point to the exit
        distance = get_distance(roads, start_brothers, exit)
        
        # Calculate the time it takes for the brothers to reach the exit at the minimum speed
        time = distance / min_speed
        
        # Calculate the time it takes for the police car to reach the exit assuming it starts moving immediately
        police_time = distance / 160
        
        # If the brothers reach the exit before the police car, update the minimum speed required to escape
        if time < police_time:
            min_speed = min(min_speed, get_speed(distance, time))
    
    # If the minimum speed is still infinite, it is impossible to escape
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

def get_distance(roads, start, end):
    # Initialize the total distance as 0
    distance = 0
    
    # Loop through all roads from the starting point to the ending point
    for road in roads:
        # If the current road connects the starting point to the ending point, update the total distance
        if road[0] == start and road[1] == end:
            distance += road[2]
    
    # Return the total distance
    return distance

def get_speed(distance, time):
    # Calculate and return the speed
    return distance / time

