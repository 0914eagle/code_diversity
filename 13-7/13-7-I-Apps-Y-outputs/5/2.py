
def get_min_cost(N, M, X, A):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (N + 1)
    # Set the initial minimum cost to 0
    min_cost[X] = 0
    
    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        current_toll_gate = A[i]
        # Loop through each square
        for j in range(N + 1):
            # If the current square is the toll gate or the previous square
            if j == current_toll_gate or j == current_toll_gate - 1:
                # Increment the minimum cost by 1
                min_cost[j] += 1
    
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

