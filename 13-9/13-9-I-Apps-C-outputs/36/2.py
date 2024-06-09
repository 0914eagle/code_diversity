
def get_min_time(start, end, conveyors):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Iterate over all possible paths from start to end
    for path in all_paths(start, end, conveyors):
        # Calculate the time for the current path
        time = path_time(path, conveyors)
        
        # Update the minimum time if necessary
        if time < min_time:
            min_time = time
    
    # Return the minimum time
    return min_time

def all_paths(start, end, conveyors):
    # Initialize the list of paths
    paths = []
    
    # Iterate over all possible combinations of conveyors
    for combination in combinations(conveyors, len(conveyors)):
        # Create a new path with the current combination of conveyors
        path = [start] + list(combination) + [end]
        
        # Add the path to the list of paths
        paths.append(path)
    
    # Return the list of paths
    return paths

def path_time(path, conveyors):
    # Initialize the time
    time = 0
    
    # Iterate over all segments in the path
    for i in range(len(path) - 1):
        # Calculate the time for the current segment
        time += segment_time(path[i], path[i + 1], conveyors)
    
    # Return the total time
    return time

def segment_time(start, end, conveyors):
    # Initialize the time
    time = 0
    
    # Iterate over all conveyors between start and end
    for conveyor in conveyors:
        # Calculate the time for the current conveyor segment
        time += conveyor_time(start, end, conveyor)
    
    # Return the total time
    return time

def conveyor_time(start, end, conveyor):
    # Calculate the distance between start and end on the conveyor
    distance = distance_on_conveyor(start, end, conveyor)
    
    # Calculate the time for the conveyor segment
    time = distance / conveyor_speed(conveyor)
    
    # Return the time
    return time

def distance_on_conveyor(start, end, conveyor):
    # Calculate the distance between start and end on the conveyor
    distance = distance_between_points(start, end) - distance_between_points(start, conveyor[0]) - distance_between_points(conveyor[1], end)
    
    # Return the distance
    return distance

def distance_between_points(p1, p2):
    # Calculate the distance between p1 and p2
    distance = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    
    # Return the distance
    return distance

def conveyor_speed(conveyor):
    # Calculate the speed of the conveyor
    speed = 2
    
    # Return the speed
    return speed

