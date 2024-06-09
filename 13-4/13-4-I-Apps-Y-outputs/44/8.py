
def solve(N, M, X, toll_gates):
    # Initialize the minimum cost to reach the goal as infinity
    min_cost = float('inf')
    # Loop through all possible starting points
    for i in range(N+1):
        # If the starting point is not the current square or a toll gate, continue
        if i == X or i in toll_gates:
            continue
        # Initialize the current cost to 0
        cost = 0
        # Loop through all possible ending points
        for j in range(N+1):
            # If the ending point is the goal or a toll gate, continue
            if j == 0 or j == N or j in toll_gates:
                continue
            # Calculate the cost of traveling from the starting point to the ending point
            cost += 1
        # If the current cost is less than the minimum cost, update the minimum cost
        if cost < min_cost:
            min_cost = cost
    # Return the minimum cost
    return min_cost

