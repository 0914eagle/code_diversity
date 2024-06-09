
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')

    # Loop through all possible routes from the brothers' starting point to the highway exits
    for exit in exits:
        # Calculate the distance from the brothers' starting point to the exit
        distance = calculate_distance(roads, start_brothers, exit)

        # Calculate the time it takes for the brothers to travel this distance at the minimum speed required to escape
        time = distance / min_speed

        # Calculate the time it takes for the police car to travel this distance at its maximum speed
        police_time = distance / 160

        # If the brothers' time is less than or equal to the police car's time, the brothers can escape
        if time <= police_time:
            # Update the minimum speed required to escape if necessary
            min_speed = min(min_speed, distance / time)

    # If the minimum speed is still infinity, it is impossible for the brothers to escape
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

def calculate_distance(roads, start, end):
    # Initialize the total distance as zero
    distance = 0

    # Loop through all the roads between the start and end points
    for road in roads:
        # If the current road connects the start and end points, add its length to the total distance
        if road[0] == start and road[1] == end:
            distance += road[2]

    # Return the total distance
    return distance

