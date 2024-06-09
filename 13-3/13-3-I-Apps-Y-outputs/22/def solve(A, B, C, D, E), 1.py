
def solve(A, B, C, D, E):
    # Calculate the time it takes to serve each dish
    time_to_serve = [A, B, C, D, E]
    
    # Find the earliest possible time for the last dish to be delivered
    earliest_time = 0
    for i in range(len(time_to_serve)):
        earliest_time += time_to_serve[i]
    
    return earliest_time

