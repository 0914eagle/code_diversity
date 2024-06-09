
def solve(n, l, v1, v2, k):
    # Calculate the time it takes for all pupils to walk
    time_walk = l / v1
    
    # Calculate the time it takes for the bus to travel the distance
    time_bus = l / v2
    
    # Calculate the number of bus rides required
    num_rides = n // k
    
    # Calculate the time it takes for the bus to make all the rides
    time_rides = time_bus * num_rides
    
    # Calculate the time it takes for the remaining pupils to walk
    time_walk_remaining = l - (k * time_bus * num_rides)
    
    # Calculate the total time required
    time_total = time_rides + time_walk_remaining
    
    return time_total

