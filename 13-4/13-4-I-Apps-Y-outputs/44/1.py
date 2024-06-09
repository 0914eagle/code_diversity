
def solve(n, m, x, a):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n+1)
    # Initialize the previous array with -1s
    prev = [-1] * (n+1)
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        current_toll_gate = a[i]
        # Loop through each square
        for j in range(n+1):
            # If the current square is the previous square of the current toll gate
            if j == prev[current_toll_gate]:
                # Update the minimum cost and previous array
                min_cost[j] += 1
                prev[j] = current_toll_gate
    # Return the minimum cost of reaching the goal
    return min_cost[x]

