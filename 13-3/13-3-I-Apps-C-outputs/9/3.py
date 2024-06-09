
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
    
    # Loop through each gate
    for i in range(1, N):
        # Loop through each pair of skis
        for j in range(S):
            # Check if the current pair of skis can pass through the current gate
            if x[i] - W <= x[i-1] + v_h * min_time_skis[(x[i-1], y[i-1])][s[j]]:
                # Calculate the minimum time required to pass through the current gate with the current pair of skis
                min_time_skis[(x[i], y[i])][s[j]] = min(min_time_skis[(x[i], y[i])][s[j]], s[j] + min_time_skis[(x[i-1], y[i-1])][s[j]])
            else:
                # If the current pair of skis cannot pass through the current gate, set the minimum time to infinity
                min_time_skis[(x[i], y[i])][s[j]] = float('inf')
    
    # Find the minimum time required to pass through all the gates with any pair of skis
    min_time = min({min_time_skis[(x[i], y[i])][s[j]] for j in range(S) for i in range(N)})
    
    # If the minimum time is infinity, it is impossible to complete the race with any pair of skis
    if min_time == float('inf'):
        return "IMPOSSIBLE"
    else:
        # Find the pair of skis that allows you to get through the race course in the shortest time
        min_skis = [s[j] for j in range(S) if min_time_skis[(x[N-1], y[N-1])][s[j]] == min_time][0]
        return min_skis

