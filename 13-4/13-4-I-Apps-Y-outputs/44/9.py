
def solve(N, M, X, A):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (N+1)
    # Initialize the previous array with -1s
    prev = [-1] * (N+1)
    
    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        curr_toll = A[i]
        # Loop through each square
        for j in range(N+1):
            # If the current square is the previous square of the current toll gate
            if j == prev[curr_toll]:
                # Update the minimum cost of the current square
                min_cost[j] += 1
            # If the current square is not the previous square of the current toll gate
            elif j != prev[curr_toll]:
                # Update the minimum cost of the current square
                min_cost[j] = min(min_cost[j], min_cost[prev[curr_toll]] + 1)
            # Update the previous square of the current toll gate
            prev[curr_toll] = j
    
    # Return the minimum cost of the goal square (either 0 or N)
    return min_cost[X]

