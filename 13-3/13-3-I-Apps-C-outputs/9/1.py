
def solve(W, v_h, N, x, y, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x[i], y[i])] = float('inf')
    
    # Initialize a dictionary to store the minimum time required to pass through each gate with each pair of skis
    min_time_skis = {}
    for i in range(N):
        min_time_skis[(x[i], y[i])] = {s[j]: float('inf') for j in range(S)}
    
    # Initialize the minimum time required to pass through the first gate with each pair of skis
    for j in range(S):
        min_time_skis[(x[0], y[0])][s[j]] = s[j]
    
    # Loop through each gate and calculate the minimum time required to pass through it with each pair of skis
    for i in range(1, N):
        for j in range(S):
            # Calculate the minimum time required to pass through the current gate with the current pair of skis
            min_time_skis[(x[i], y[i])][s[j]] = min(min_time_skis[(x[i], y[i])][s[j]], min_time_skis[(x[i-1], y[i-1])][s[j]] + max(0, s[j] - (x[i] - x[i-1])))
        
            # Calculate the minimum time required to pass through the current gate with any pair of skis
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], min(min_time_skis[(x[i], y[i])].values()))
    
    # Find the pair of skis that allows you to get through the race course in the shortest time
    min_time_skis_sorted = sorted(min_time_skis[(x[N-1], y[N-1])].items(), key=lambda x: x[1])
    if min_time_skis_sorted[0][1] == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_time_skis_sorted[0][0]

