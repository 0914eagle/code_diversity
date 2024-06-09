
def solve(n, m, x, a):
    # Initialize the minimum cost array with 0 for all squares
    min_cost = [0] * (n+1)
    # Initialize the previous square array with -1 for all squares
    prev_square = [-1] * (n+1)
    
    # Set the initial square as the starting square
    curr_square = x
    
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        toll_gate = a[i]
        
        # Loop through each square
        for j in range(n+1):
            # If the current square is the toll gate, update the minimum cost and previous square
            if j == toll_gate:
                min_cost[j] = 1
                prev_square[j] = curr_square
            # If the current square is not the toll gate, update the minimum cost based on the previous square
            else:
                min_cost[j] = min(min_cost[j], min_cost[curr_square] + 1)
    
    # Return the minimum cost of reaching the goal
    return min_cost[n]

