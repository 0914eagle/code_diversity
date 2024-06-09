
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimal speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exits
    for exit in exits:
        # Calculate the distance from the brothers' starting point to the current highway exit
        distance = calculate_distance(roads, start_brothers, exit)
        
        # Calculate the speed required to escape given the distance and the maximum speed of the police car
        speed = calculate_speed(distance, 160)
        
        # Update the minimal speed required to escape if the current speed is lower than the previous minimum
        min_speed = min(min_speed, speed)
    
    # Return the minimal speed required to escape or the word "IMPOSSIBLE" if it is impossible
    return "IMPOSSIBLE" if min_speed == float('inf') else min_speed

# Calculate the distance from a starting point to a destination point using a list of roads
def calculate_distance(roads, start, destination):
    # Initialize the distance as zero
    distance = 0
    
    # Loop through all roads from the starting point to the destination point
    for road in roads:
        # If the current road is the one leading to the destination point, add its length to the distance
        if road[0] == start and road[1] == destination:
            distance += road[2]
    
    # Return the distance
    return distance

# Calculate the speed required to escape given a distance and a maximum speed
def calculate_speed(distance, max_speed):
    # Initialize the speed as the maximum speed
    speed = max_speed
    
    # Loop until the speed is low enough to cover the distance
    while speed * distance > 160:
        # Decrease the speed by 1 km/h
        speed -= 1
    
    # Return the speed
    return speed

