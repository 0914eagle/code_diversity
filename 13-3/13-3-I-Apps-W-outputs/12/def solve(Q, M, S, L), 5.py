
def solve(Q, M, S, L):
    # Calculate the total number of time slots
    total_slots = S + L * Q
    
    # Initialize the minimum time to complete all slots
    min_time = float('inf')
    
    # Iterate through all possible combinations of machines and time slots
    for i in range(1, M + 1):
        for j in range(1, total_slots // i + 1):
            # Calculate the time to complete the current combination of machines and time slots
            time = i * j
            
            # Check if the current combination is the minimum time to complete all slots
            if time < min_time:
                min_time = time
    
    return min_time

