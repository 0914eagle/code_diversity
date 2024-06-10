
def get_min_cost(N, M, X, A):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (N + 1)
    # Initialize the previous array with -1s
    prev = [-1] * (N + 1)
    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        curr_toll_gate = A[i]
        # Loop through each square
        for j in range(N + 1):
            # If the current square is the toll gate or the previous square
            if j == curr_toll_gate or j == prev[curr_toll_gate]:
                # Increment the minimum cost by 1
                min_cost[j] += 1
            # If the current square is not the toll gate or the previous square
            else:
                # Update the minimum cost and previous array
                min_cost[j] = min(min_cost[j], min_cost[prev[j]] + 1)
                prev[j] = prev[prev[j]]
    # Return the minimum cost of reaching the goal
    return min_cost[X]

def main():
    # Read the input
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    # Call the get_min_cost function
    cost = get_min_cost(N, M, X, A)
    # Print the minimum cost
    print(cost)

if __name__ == '__main__':
    main()

