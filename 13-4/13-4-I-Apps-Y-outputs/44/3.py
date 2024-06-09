
def solve(n, m, x, toll_gates):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n+1)
    # Initialize the previous array with -1s
    prev = [-1] * (n+1)
    
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        curr_toll_gate = toll_gates[i]
        # Loop through each square
        for j in range(n+1):
            # Check if the current square is the previous square of the current toll gate
            if j == prev[curr_toll_gate]:
                # Update the minimum cost for the current square
                min_cost[j] += 1
    
    # Loop through each square
    for i in range(n+1):
        # Check if the current square is the starting square
        if i == x:
            # Update the previous array with the starting square
            prev[i] = x
        # Loop through each toll gate
        for j in range(m):
            # Get the current toll gate
            curr_toll_gate = toll_gates[j]
            # Check if the current square is the previous square of the current toll gate
            if i == prev[curr_toll_gate]:
                # Update the previous array with the previous square of the current toll gate
                prev[i] = prev[curr_toll_gate]
    
    # Return the minimum cost for the goal square (either 0 or N)
    return min_cost[0] if x == 0 else min_cost[n]

