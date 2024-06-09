
def solve(n, l, v1, v2, k):
    # Calculate the time it takes for all pupils to walk
    time_walk = l / v1
    
    # Calculate the time it takes for the bus to travel the distance
    time_bus = l / v2
    
    # Calculate the number of bus trips needed
    num_trips = n // k
    
    # Calculate the time it takes for the bus to make all the trips
    time_bus_trips = time_bus * num_trips
    
    # Calculate the time it takes for the pupils to walk to the bus stop and back
    time_walk_to_bus = (n % k) * (time_walk / num_trips)
    
    # Calculate the total time
    total_time = time_bus_trips + time_walk_to_bus
    
    return total_time

