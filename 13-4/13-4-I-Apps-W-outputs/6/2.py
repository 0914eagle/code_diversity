
def get_min_draws(N, squares):
    # Initialize a dictionary to store the minimum number of draws required to reach each square
    min_draws = {0: 0}
    for i in range(1, N+1):
        min_draws[i] = float('inf')

    # Loop through each square and calculate the minimum number of draws required to reach it
    for i in range(1, N+1):
        for j in range(i-1, -1, -1):
            if squares[j] == squares[i]:
                min_draws[i] = min(min_draws[i], min_draws[j] + 1)
                break

    return min_draws[N]

