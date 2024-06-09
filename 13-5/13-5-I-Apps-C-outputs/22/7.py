
def escape_speed(intersections, roads, exits, brothers_start, police_start):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')
    
    # Loop through all possible routes from the brothers' starting intersection to the highway exits
    for exit in exits:
        # Find the shortest path from the brothers' starting intersection to the highway exit using Dijkstra's algorithm
        path = dijkstra(intersections, roads, brothers_start, exit)
        
        # If a path exists, calculate the speed required to escape
        if path:
            # Calculate the distance from the brothers' starting intersection to the highway exit
            distance = 0
            for i in range(len(path) - 1):
                distance += roads[path[i]][path[i+1]]['length']
            
            # Calculate the time required to travel the distance at the maximum speed of the police car
            time = distance / 160
            
            # Calculate the speed required to escape by subtracting the time required to travel the distance from the maximum speed of the police car
            speed = 160 - time
            
            # Update the minimum speed required to escape if the current speed is lower
            min_speed = min(min_speed, speed)
    
    # If a route exists, return the minimum speed required to escape
    if min_speed < float('inf'):
        return min_speed
    # Otherwise, return the word "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

