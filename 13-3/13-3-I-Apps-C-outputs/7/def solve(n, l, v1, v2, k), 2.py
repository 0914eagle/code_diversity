
def solve(n, l, v1, v2, k):
    # Calculate the time it takes for all pupils to walk
    time_walk = l / v1
    
    # Calculate the number of bus rides needed
    num_rides = n // k
    
    # Calculate the time it takes for each bus ride
    time_ride = l / v2
    
    # Calculate the total time it takes for all pupils to reach the place of excursion
    total_time = time_walk + num_rides * time_ride
    
    return total_time

