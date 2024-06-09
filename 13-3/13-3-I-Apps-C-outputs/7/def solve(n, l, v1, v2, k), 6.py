
def solve(n, l, v1, v2, k):
    # Calculate the time it takes for all pupils to walk
    time_walk = l / v1
    
    # Calculate the time it takes for the bus to travel the distance
    time_bus = l / v2
    
    # Calculate the number of buses needed
    num_buses = n // k
    
    # Calculate the time it takes for the buses to travel the distance
    time_buses = time_bus * num_buses
    
    # Calculate the total time
    total_time = time_walk + time_buses
    
    return total_time

