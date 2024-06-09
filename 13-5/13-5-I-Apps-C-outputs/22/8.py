
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimal speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exits
    for exit in exits:
        # Calculate the distance from the brothers' starting point to the current highway exit
        distance = calculate_distance(start_brothers, exit, roads)
        
        # Calculate the time it takes for the brothers to reach the highway exit at the minimal speed required to escape
        time = distance / min_speed
        
        # Calculate the time it takes for the police car to reach the highway exit from the police station
        police_time = calculate_time(start_police, exit, roads, 160)
        
        # If the brothers reach the highway exit before the police car, update the minimal speed required to escape
        if time < police_time:
            min_speed = min(min_speed, distance / time)
    
    # If the minimal speed required to escape is infinity, return "IMPOSSIBLE"
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

# Calculate the distance between two intersections
def calculate_distance(start, end, roads):
    distance = 0
    current = start
    while current != end:
        for road in roads:
            if road[0] == current and road[1] == end:
                distance += road[2]
                current = end
                break
            elif road[0] == current and road[1] != end:
                distance += road[2]
                current = road[1]
                break
    return distance

# Calculate the time it takes for a car to reach a destination at a given speed
def calculate_time(start, end, roads, speed):
    distance = calculate_distance(start, end, roads)
    time = distance / speed
    return time

