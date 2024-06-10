
def get_min_cost(N, M, X, A):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (N + 1)
    # Set the initial minimum cost to 0
    min_cost[X] = 0
    
    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        curr_toll_gate = A[i]
        # Loop through each square
        for j in range(N + 1):
            # If the current square is not the toll gate and the minimum cost of reaching the current square is not 0
            if j != curr_toll_gate and min_cost[j] != 0:
                # Set the minimum cost of the current square to the minimum of the current cost and the cost of reaching the current square + 1
                min_cost[j] = min(min_cost[j], min_cost[curr_toll_gate] + 1)
    
    # Return the minimum cost of reaching the goal
    return min_cost[N]

def main():
    # Read the input data
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Get the minimum cost
    min_cost = get_min_cost(N, M, X, A)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

