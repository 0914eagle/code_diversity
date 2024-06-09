
def solve(Q, M, S, L):
    # Calculate the total number of time slots
    total_slots = S + L * Q
    
    # Calculate the minimum number of machines needed to complete all time slots
    min_machines = total_slots // M
    
    # Calculate the number of time slots that cannot be completed on the minimum number of machines
    extra_slots = total_slots % M
    
    # Calculate the minimum time needed to complete all time slots
    min_time = min_machines * M
    
    # If there are extra time slots, add the time needed to complete them on an additional machine
    if extra_slots > 0:
        min_time += extra_slots
    
    return min_time

