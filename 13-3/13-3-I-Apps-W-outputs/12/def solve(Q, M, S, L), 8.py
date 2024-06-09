
def solve(Q, M, S, L):
    # Calculate the total number of time slots
    total_slots = S + L * Q
    
    # Calculate the minimum number of machines needed to complete all time slots
    min_machines = total_slots // M
    
    # Calculate the number of time slots that cannot be completed on the minimum number of machines
    extra_slots = total_slots % M
    
    # If there are no extra time slots, return the minimum number of machines needed
    if extra_slots == 0:
        return min_machines
    
    # If there are extra time slots, return the minimum number of machines needed plus one
    return min_machines + 1

