
def get_min_cost(n, m, x, toll_gates):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n + 1)
    # Set the initial cost to 0
    min_cost[x] = 0
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        current_toll_gate = toll_gates[i]
        # Loop through each square
        for j in range(n + 1):
            # Check if the current square is the toll gate or the previous square
            if j == current_toll_gate or j == x:
                continue
            # Update the minimum cost for the current square
            min_cost[j] = min(min_cost[j], min_cost[current_toll_gate] + 1)
    # Return the minimum cost for the goal square
    return min_cost[n]

def main():
    # Read the input data
    n, m, x = map(int, input().split())
    toll_gates = list(map(int, input().split()))
    # Call the get_min_cost function
    min_cost = get_min_cost(n, m, x, toll_gates)
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

