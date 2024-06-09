
def solve(n, l, v1, v2, k):
    # Calculate the time it takes for the bus to travel the distance
    bus_time = l / v2
    
    # Calculate the number of buses needed to transport all pupils
    num_buses = n // k
    
    # Calculate the time it takes for the pupils to travel to the buses
    pupil_time = n / v1
    
    # Calculate the total time it takes for all pupils to reach the place of excursion
    total_time = bus_time * num_buses + pupil_time
    
    return total_time

