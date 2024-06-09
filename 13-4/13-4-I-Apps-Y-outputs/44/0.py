
def solve(n, m, x, a):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n+1)
    # Initialize the previous array with -1s
    prev = [-1] * (n+1)
    # Set the initial minimum cost to 0 and previous square to -1
    min_cost[x] = 0
    prev[x] = -1
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        curr_toll = a[i]
        # Loop through each square
        for j in range(n+1):
            # Check if the current square is not the previous square and has a higher cost than the current minimum cost
            if j != prev[x] and min_cost[j] > min_cost[x] + 1:
                # Update the minimum cost and previous square
                min_cost[j] = min_cost[x] + 1
                prev[j] = x
    # Return the minimum cost of reaching the goal
    return min_cost[n]

