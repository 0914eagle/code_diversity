
def get_min_cost(n, m, x, a):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n + 1)
    # Set the initial minimum cost to 0
    min_cost[x] = 0
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        current_toll_gate = a[i]
        # Loop through each square
        for j in range(n + 1):
            # Check if the current square has a toll gate
            if j == current_toll_gate:
                # If the current square has a toll gate, set the minimum cost to 1
                min_cost[j] = 1
            # Check if the current square is adjacent to the current toll gate
            if j == current_toll_gate - 1 or j == current_toll_gate + 1:
                # If the current square is adjacent to the current toll gate, set the minimum cost to 1 + the current minimum cost
                min_cost[j] = 1 + min_cost[current_toll_gate]
    # Return the minimum cost of reaching the goal
    return min_cost[n]

def main():
    # Read the input data
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    # Get the minimum cost
    min_cost = get_min_cost(n, m, x, a)
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

