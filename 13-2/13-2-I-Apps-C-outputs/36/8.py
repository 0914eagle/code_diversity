
def escape_speed(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimal speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting point to the highway exits
    for exit in exits:
        # Calculate the distance from the brothers' starting point to the highway exit
        distance = 0
        current_point = start_brothers
        while current_point != exit:
            # Find the next road in the route
            next_road = None
            for road in roads:
                if road[0] == current_point and road[1] == exit:
                    next_road = road
                    break
            if next_road is None:
                # If there is no road between the current point and the exit, the route is not possible
                break
            # Add the length of the next road to the total distance
            distance += next_road[2]
            # Update the current point to the end of the next road
            current_point = next_road[1]
        
        # If the route is possible, calculate the speed required to escape
        if current_point == exit:
            # Calculate the time it takes for the brothers to travel the route
            time = distance / 160
            # Calculate the speed required to escape
            speed = distance / time
            # Update the minimal speed required to escape if necessary
            if speed < min_speed:
                min_speed = speed
    
    # Return the minimal speed required to escape or the word IMPOSSIBLE if it is impossible
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

