
def solve(n, m, x, a):
    # Initialize the minimum cost array with 0 for the starting square
    min_cost = [0] * (n+1)
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate and the next toll gate
        current_toll_gate = a[i]
        next_toll_gate = a[i+1] if i < m-1 else -1
        # Loop through each square
        for j in range(n+1):
            # If the current square is the starting square or the next toll gate, skip it
            if j == x or j == current_toll_gate or j == next_toll_gate:
                continue
            # If the current square is between the current toll gate and the next toll gate, update the minimum cost
            if current_toll_gate < j < next_toll_gate:
                min_cost[j] = 1
    # Return the minimum cost of reaching the goal
    return min_cost[n]

