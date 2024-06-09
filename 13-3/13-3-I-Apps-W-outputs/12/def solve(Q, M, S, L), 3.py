
def solve(Q, M, S, L):
    # Calculate the total number of time slots
    total_slots = S + L * Q
    
    # Calculate the minimum number of machines needed to complete all time slots
    min_machines = (total_slots + M - 1) // M
    
    # Calculate the minimum time needed to complete all time slots
    min_time = min_machines * Q
    
    return min_time

