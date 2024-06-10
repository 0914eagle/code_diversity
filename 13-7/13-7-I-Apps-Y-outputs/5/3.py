
def get_min_cost(N, M, X, toll_gates):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (N + 1)
    # Set the initial minimum cost to 0
    min_cost[X] = 0
    
    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        current_toll_gate = toll_gates[i]
        # Loop through each square
        for j in range(N + 1):
            # Check if the current square is the previous toll gate
            if j == current_toll_gate:
                # Skip this square
                continue
            # Check if the current square is not the goal square
            if j != 0 and j != N:
                # Update the minimum cost for this square
                min_cost[j] = min(min_cost[j], min_cost[j - 1] + 1)
    
    # Return the minimum cost for the goal square
    return min_cost[N]

def main():
    # Read the input data
    N, M, X = map(int, input().split())
    toll_gates = list(map(int, input().split()))
    
    # Get the minimum cost
    min_cost = get_min_cost(N, M, X, toll_gates)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

